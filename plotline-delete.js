(function () {
  'use strict';
  const de = document.documentElement.lang === 'de';
  const config = {...(window.PLOTLINE_CONFIG || {})};
  const $ = id => document.getElementById(id);
  const text = (g, e) => de ? g : e;
  let identity = null, receipt = null, deleting = false;
  const show = message => { $('result').textContent = message; };
  function hex() { return Array.from(crypto.getRandomValues(new Uint8Array(32)), b => b.toString(16).padStart(2, '0')).join(''); }
  async function api(path, method = 'POST', body, token) {
    const response = await fetch(config.apiBase + '/v2/' + path, {
      method, mode: 'cors', credentials: 'omit', cache: 'no-store', redirect: 'error',
      headers: {'content-type': 'application/json', ...(token ? {authorization: 'Bearer ' + token} : {})},
      ...(body === undefined ? {} : {body: JSON.stringify(body)}), signal: AbortSignal.timeout(30000)
    });
    const value = await response.json();
    if (!response.ok) throw new Error(response.status === 401 ? 'reauthenticate' : 'request_failed');
    return value;
  }
  function loadScript(url) {
    return new Promise((resolve, reject) => {
      const script = document.createElement('script'); script.src = url;
      script.referrerPolicy = 'no-referrer'; script.onload = resolve; script.onerror = reject;
      document.head.appendChild(script);
    });
  }
  async function login(provider, credential, nonce, authorizationCode) {
    const value = await api('auth/login', 'POST', {provider, idToken: credential, nonce,
      ...(provider === 'apple' ? {web: true, authorizationCode} : {})});
    if (!/^[a-f0-9-]{36}$/.test(value.accountId) || typeof value.token !== 'string' ||
        !value.token.startsWith(value.accountId + '.') || !Number.isSafeInteger(value.expiresAt)) throw new Error('invalid_identity');
    identity = {provider, token: value.token, accountId: value.accountId}; receipt = null;
    $('sign-in').hidden = true; $('confirmation').hidden = false;
    $('confirm-delete').checked = false; $('delete-account').disabled = true;
    $('identity').textContent = text('Angemeldet mit ', 'Signed in with ') + (provider === 'apple' ? 'Apple' : 'Google');
    show(text('Prüfe die Löschhinweise und bestätige deinen Wunsch.', 'Review the deletion notice and confirm your choice.'));
  }
  function fail(error) {
    show(error.message === 'reauthenticate' ? text('Bitte melde dich erneut an, um die Löschung zu bestätigen.', 'Please sign in again to confirm deletion.') : text('Der Auftrag konnte nicht bestätigt werden. Prüfe deine Verbindung und versuche es erneut.', 'The request could not be confirmed. Check your connection and try again.'));
  }
  function reset() {
    identity = null; $('confirmation').hidden = true; $('sign-in').hidden = false;
    $('confirm-delete').checked = false; $('delete-account').disabled = true;
    $('google-button').replaceChildren();
  }
  async function check() {
    if (!receipt) return false;
    const value = await api('account/deletion-status', 'POST', {accountId: receipt.accountId, receipt: receipt.receipt});
    if (!['deleting', 'deleted'].includes(value.status)) throw new Error('invalid_status');
    show(value.status === 'deleted' ? text('Die Online-Daten wurden gelöscht. Minimale Nachweise bleiben wie beschrieben erhalten.', 'Online data has been deleted. Minimal records remain as described.') : text('Dein Konto ist gesperrt. Die Löschung wird automatisch abgeschlossen; du kannst den Status später erneut prüfen.', 'Your account is blocked. Deletion will complete automatically; you can check again later.'));
    $('receipt-actions').hidden = false; return true;
  }
  function configured() {
    try {
      const url = new URL(config.apiBase);
      return config.enabled === true && url.protocol === 'https:' && !url.username && !url.password && !url.search && !url.hash && url.pathname === '/';
    } catch (_) { return false; }
  }
  if (!configured()) { $('receipt-import-label').hidden = true; return; }
  config.apiBase = config.apiBase.replace(/\/$/, '');
  $('availability').textContent = text('Die Löschung läuft automatisch. Eine Kontaktaufnahme ist im normalen Ablauf nicht nötig.', 'Deletion is automatic. The normal process does not require contacting support.');
  $('sign-in').hidden = false;
  $('google-start').hidden = !config.googleClientId;
  $('apple-start').hidden = !config.appleClientId || !config.appleRedirectURI;
  $('google-start').addEventListener('click', async () => {
    try {
      const {nonce} = await api('auth/challenge', 'POST', {provider: 'google'});
      if (!window.google?.accounts?.id) await loadScript('https://accounts.google.com/gsi/client');
      google.accounts.id.initialize({client_id: config.googleClientId, nonce, auto_select: false,
        callback: async response => { try { await login('google', response.credential, nonce); } catch (e) { fail(e); } }});
      google.accounts.id.renderButton($('google-button'), {type: 'standard', theme: 'outline', size: 'large'});
    } catch (e) { fail(e); }
  });
  $('apple-start').addEventListener('click', async () => {
    try {
      const {nonce} = await api('auth/challenge', 'POST', {provider: 'apple'}), state = hex();
      if (!window.AppleID) await loadScript('https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js');
      AppleID.auth.init({clientId: config.appleClientId, redirectURI: config.appleRedirectURI, nonce, state, usePopup: true});
      const response = await AppleID.auth.signIn();
      if (response.authorization.state !== state) throw new Error('state_mismatch');
      await login('apple', response.authorization.id_token, nonce, response.authorization.code);
    } catch (e) { fail(e); }
  });
  $('confirm-delete').addEventListener('change', () => { $('delete-account').disabled = !identity || !$('confirm-delete').checked || deleting; });
  $('delete-account').addEventListener('click', async () => {
    if (!identity || !$('confirm-delete').checked || deleting) return;
    deleting = true; $('delete-account').disabled = true;
    receipt ||= {version: 1, accountId: identity.accountId, receipt: hex(), apiBase: config.apiBase, createdAt: Date.now()};
    $('receipt-actions').hidden = false;
    try {
      const value = await api('account', 'DELETE', {receipt: receipt.receipt}, identity.token);
      if (value.status !== 'deleting') throw new Error('invalid_status');
      reset(); await check();
    } catch (e) {
      try { if (await check()) reset(); } catch (_) { fail(e); }
    } finally {
      deleting = false; $('delete-account').disabled = !identity || !$('confirm-delete').checked;
    }
  });
  $('status').addEventListener('click', async () => { try { await check(); } catch (_) { show(text('Der Löschstatus ist gerade nicht erreichbar oder der Beleg ist abgelaufen. Versuche es später erneut; ein abgelaufener Beleg bedeutet nicht, dass die Löschung rückgängig gemacht wurde.', 'The status is unavailable or the receipt has expired. Try again later; expiry does not mean deletion was reversed.')); } });
  $('cancel').addEventListener('click', async () => {
    const token = identity?.token; reset();
    if (token) { try { await api('auth/logout', 'POST', {}, token); } catch (_) {} }
    show(text('Abgemeldet. Es wurde kein neuer Löschauftrag gesendet.', 'Signed out. No new deletion request was sent.'));
  });
  $('save-receipt').addEventListener('click', () => {
    if (!receipt) return;
    const url = URL.createObjectURL(new Blob([JSON.stringify(receipt)], {type: 'application/json'}));
    const link = document.createElement('a'); link.href = url; link.download = 'plotline-deletion-receipt.json'; link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  });
  $('receipt-import').addEventListener('change', async event => {
    try {
      const file = event.target.files?.[0]; if (!file || file.size > 4096) throw new Error('invalid_receipt');
      const value = JSON.parse(await file.text());
      if (value.version !== 1 || value.apiBase !== config.apiBase || !/^[a-f0-9-]{36}$/.test(value.accountId) || !/^[a-f0-9]{64}$/.test(value.receipt)) throw new Error('invalid_receipt');
      receipt = value; await check();
    } catch (_) { show(text('Der Beleg konnte nicht geprüft werden. Nutze die unveränderte Datei aus diesem Dienst.', 'The receipt could not be checked. Use the unchanged file from this service.')); }
  });
})();
