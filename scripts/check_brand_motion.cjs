// Behavior checks for lazy loading and the static-image accessibility fallback.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = fs.readFileSync(path.join(__dirname, '../site.js'), 'utf8');
const code = source.slice(source.indexOf('// Progressive enhancement:'));

function setup({ reduce = false, observer = true } = {}) {
  const images = [], parents = [], observers = [];
  class Element {
    constructor() {
      this.children = [];
      this.classes = new Set();
      this.classList = { add: value => this.classes.add(value), remove: value => this.classes.delete(value) };
    }
    appendChild(child) {
      child.remove();
      this.children.push(child);
      child.parentNode = this;
    }
    insertBefore(child, before) {
      this.children.splice(this.children.indexOf(before), 0, child);
      child.parentNode = this;
    }
    remove() {
      if (this.parentNode) {
        this.parentNode.children = this.parentNode.children.filter(child => child !== this);
        this.parentNode = null;
      }
    }
    setAttribute(name, value) { this[name] = value; }
    querySelector() { return this.children.find(child => child.className === 'app-brand-animation'); }
  }
  const icons = ['loern-icon-7d9d53a', 'sudoku-icon', 'tower-icon'].map(name => {
    const parent = new Element(), icon = new Element();
    icon.src = `https://example.com/pictures/${name}.png`;
    parent.appendChild(icon);
    parents.push(parent);
    return icon;
  });
  const preference = { matches: reduce, addEventListener: (_, callback) => preference.change = callback };
  class Observer {
    constructor(callback) { this.callback = callback; this.observed = new Set(); observers.push(this); }
    observe(icon) { this.observed.add(icon); }
    unobserve(icon) { this.observed.delete(icon); }
    disconnect() { this.observed.clear(); }
    intersect(isIntersecting = true) {
      this.callback([...this.observed].map(target => ({ target, isIntersecting })));
    }
  }
  class Image extends Element { constructor() { super(); images.push(this); } }
  vm.runInNewContext(code, {
    window: { matchMedia: () => preference, IntersectionObserver: observer ? Observer : undefined },
    IntersectionObserver: Observer, Image, URL,
    document: { querySelectorAll: () => icons, createElement: () => new Element() },
  });
  return { images, icons, parents, observers, preference };
}

for (const options of [{ reduce: true }, { observer: false }]) {
  const s = setup(options);
  assert.equal(s.images.length, 0);
  assert.equal(s.observers.length, 0);
  s.parents.forEach((parent, i) => assert.equal(parent.children[0], s.icons[i]));
}
{
  const s = setup(), observer = s.observers[0];
  assert.equal(s.images.length, 0, 'No animation requests before icons enter the viewport');
  observer.intersect(false);
  assert.equal(s.images.length, 0);
  observer.intersect();
  assert.equal(s.images.length, 3);
  s.images.forEach((image, i) => {
    assert.equal(image.alt, '');
    assert.equal(image['aria-hidden'], 'true');
    assert.equal(image.parentNode.classes.has('is-playing'), false);
    image.onload();
    assert.equal(image.parentNode.classes.has('is-playing'), true);
    assert.equal(image.src, `https://example.com/pictures/brand/${['loern', 'sudoku', 'tower'][i]}-splash.svg`);
  });
  observer.intersect();
  assert.equal(s.images.length, 3, 'No replay when scrolling away and back');
  s.preference.matches = true;
  s.preference.change({ matches: true });
  s.parents.forEach(parent => {
    const wrapper = parent.children[0];
    assert.equal(wrapper.classes.has('is-playing'), false);
    assert.equal(wrapper.children.length, 1);
  });
  // A late load callback must not hide the fallback after its overlay was removed.
  s.preference.matches = false;
  s.images.forEach(image => image.onload());
  s.parents.forEach(parent => assert.equal(parent.children[0].classes.has('is-playing'), false));
}
{
  const s = setup();
  s.observers[0].intersect();
  s.images.forEach(image => image.onerror());
  s.parents.forEach((parent, i) => {
    assert.equal(parent.children[0].classes.has('is-playing'), false);
    assert.equal(parent.children[0].children[0], s.icons[i]);
  });
}
console.log('PASS: reduced motion, unsupported observer, lazy loading, one-shot playback, preference changes, late loads, failed images');
