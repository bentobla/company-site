const {test} = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const {webcrypto} = require('node:crypto');
const source = fs.readFileSync('plotline-delete.js', 'utf8');
const owner = '11111111-1111-4111-a111-111111111111';
function fixture(overrides={}, handler=()=>Response.json({}), AppleID) {
  const nodes = new Map(), requests=[]; let googleCallback;
  function node(id) { if (!nodes.has(id)) nodes.set(id, {hidden:true, checked:false, disabled:true,textContent:'',listeners:{},addEventListener(type,fn){this.listeners[type]=fn;},replaceChildren(){}}); return nodes.get(id); }
  const google={accounts:{id:{initialize(value){googleCallback=value.callback;assert.equal(value.auto_select,false);},renderButton(){}}}};
  const window={AppleID,PLOTLINE_CONFIG:Object.freeze({enabled:true,apiBase:'https://api.example.test',googleClientId:'public-id',...overrides}),google};
  const context=vm.createContext({window,google,AppleID,crypto:webcrypto,Uint8Array,URL,Blob,AbortSignal,setTimeout,document:{documentElement:{lang:'en'},getElementById:node,head:{appendChild(){throw Error('Unexpected SDK load');}},createElement(){return {}; }},fetch:async(url,options)=>{requests.push({url,options});assert.equal(options.credentials,'omit');assert.equal(options.redirect,'error');return handler(url,options);}});
  vm.runInContext(source,context);
  return {node,requests,click:async id=>node(id).listeners.click?.(),change:async(id,event)=>node(id).listeners.change?.(event),login:async()=>{await node('google-start').listeners.click();await googleCallback({credential:'id-token'});}};
}
function auth(url) {
 if(url.endsWith('/auth/challenge'))return Response.json({nonce:'a'.repeat(64)});
 if(url.endsWith('/auth/login'))return Response.json({accountId:owner,token:owner+'.SECRET',expiresAt:Date.now()+300000});
 return Response.json({});
}
test('disabled and unsafe configurations load no SDK and issue no requests',async()=>{
 for(const config of [{enabled:false},{apiBase:'http://api.example.test'},{apiBase:'https://api.example.test/path'},{apiBase:'https://user:password@api.example.test'}]){
  const f=fixture(config);assert.equal(f.node('sign-in').hidden,true);assert.equal(f.node('receipt-import-label').hidden,true);await f.click('google-start');assert.equal(f.requests.length,0);
 }
});
test('sign-in alone and an unchecked confirmation cannot delete an account',async()=>{
 const f=fixture({},auth);await f.login();await f.click('delete-account');assert.equal(f.requests.length,2);assert.equal(f.node('delete-account').disabled,true);
});
test('confirmed deletion sends fresh secret receipt, status uses no bearer token',async()=>{
 const f=fixture({},(url,opts)=>url.endsWith('/v2/account')?Response.json({status:'deleting'},{status:202}):url.endsWith('/deletion-status')?Response.json({status:'deleted'}):auth(url));
 await f.login();f.node('confirm-delete').checked=true;await f.change('confirm-delete');await f.click('delete-account');
 const deletion=f.requests.find(r=>r.options.method==='DELETE');assert.match(JSON.parse(deletion.options.body).receipt,/^[a-f0-9]{64}$/);
 assert.equal(deletion.options.headers.authorization,'Bearer '+owner+'.SECRET');
 const status=f.requests.find(r=>r.url.endsWith('/deletion-status'));assert.equal(status.options.headers.authorization,undefined);assert.equal(JSON.parse(status.options.body).accountId,owner);
 assert.match(f.node('result').textContent,/has been deleted/);assert.equal(f.node('confirmation').hidden,true);
});
test('lost delete response is recovered through the same receipt',async()=>{
 let lost;
 const f=fixture({},(url,opts)=>{if(opts.method==='DELETE'){lost=JSON.parse(opts.body).receipt;throw Error('connection lost');}if(url.endsWith('/deletion-status')){assert.equal(JSON.parse(opts.body).receipt,lost);return Response.json({status:'deleting'});}return auth(url);});
 await f.login();f.node('confirm-delete').checked=true;await f.click('delete-account');assert.match(f.node('result').textContent,/automatically/);assert.equal(f.node('confirmation').hidden,true);
});
test('failed deletion and invalid status never report success and can be retried',async()=>{
 const f=fixture({},url=>url.endsWith('/v2/account')?Response.json({},{status:503}):url.endsWith('/deletion-status')?Response.json({status:'unknown'}):auth(url));
 await f.login();f.node('confirm-delete').checked=true;await f.click('delete-account');assert.match(f.node('result').textContent,/could not be confirmed/);assert.equal(f.node('delete-account').disabled,false);assert.equal(f.node('confirmation').hidden,false);
});
test('receipt import rejects another API origin before making any request',async()=>{
 const f=fixture();await f.change('receipt-import',{target:{files:[{size:100,text:async()=>JSON.stringify({version:1,apiBase:'https://evil.test',accountId:owner,receipt:'b'.repeat(64)})}]}});assert.equal(f.requests.length,0);assert.match(f.node('result').textContent,/could not be checked/);
});
test('cancel clears identity and logs out without requesting deletion',async()=>{
 const f=fixture({},auth);await f.login();await f.click('cancel');assert.equal(f.requests.at(-1).url,'https://api.example.test/v2/auth/logout');f.node('confirm-delete').checked=true;await f.click('delete-account');assert.equal(f.requests.filter(r=>r.options.method==='DELETE').length,0);
});

test('Apple web login exchanges its code and binds the popup state and nonce',async()=>{
 let setup;
 const apple={auth:{init(options){setup=options;},signIn:async()=>({authorization:{state:setup.state,id_token:'apple-id-token',code:'one-use-code'}})}};
 const f=fixture({appleClientId:'services-id',appleRedirectURI:'https://site.example.test/deletion'},url=>auth(url),apple);
 await f.click('apple-start');
 assert.equal(setup.clientId,'services-id');assert.equal(setup.nonce,'a'.repeat(64));assert.match(setup.state,/^[a-f0-9]{64}$/);
 const login=JSON.parse(f.requests.find(r=>r.url.endsWith('/auth/login')).options.body);
 assert.equal(login.provider,'apple');assert.equal(login.web,true);assert.equal(login.authorizationCode,'one-use-code');assert.equal(login.idToken,'apple-id-token');
 assert.equal(f.node('confirmation').hidden,false);assert.equal(f.requests.filter(r=>r.options.method==='DELETE').length,0);
});
test('Apple popup state mismatch never creates an app login or deletes data',async()=>{
 const apple={auth:{init(){},signIn:async()=>({authorization:{state:'foreign-state',id_token:'untrusted',code:'untrusted'}})}};
 const f=fixture({appleClientId:'services-id',appleRedirectURI:'https://site.example.test/deletion'},auth,apple);
 await f.click('apple-start');assert.equal(f.requests.length,1);assert.equal(f.node('confirmation').hidden,true);assert.match(f.node('result').textContent,/could not be confirmed/);
});
