(function () {
  "use strict";

  function ensureAppPrivacyNoindex() {
    var p = (window.location.pathname || "/").toLowerCase();
    if (!p.endsWith("/projects/loern/privacy.html") && !p.endsWith("/projects/sudoku/privacy.html")) return;
    var robots = document.querySelector('meta[name="robots"]');
    if (!robots) {
      robots = document.createElement("meta");
      robots.name = "robots";
      document.head.appendChild(robots);
    }
    robots.content = "noindex,follow";
  }

  function appendJsonLd(data) {
    var script = document.createElement("script");
    script.type = "application/ld+json";
    script.text = JSON.stringify(data);
    document.head.appendChild(script);
  }

  function addStructuredData() {
    var p = (window.location.pathname || "/").toLowerCase();
    var canonical = document.querySelector('link[rel="canonical"]');
    var metaDescription = document.querySelector('meta[name="description"]');
    var url = canonical ? canonical.href : window.location.href.split("#")[0];
    var description = metaDescription ? metaDescription.content : "";
    var organization = {
      "@type": "Organization",
      "name": "Jetzt & Dahanna Technologies",
      "url": "https://jetztunddahanna.com/",
      "founder": { "@type": "Person", "name": "Tobias Blankenhorn" }
    };

    if (/\/(de|en|fr|es|it|nl|sv|pl|pt-br|pt-pt)\/$/.test(p)) {
      appendJsonLd(Object.assign({ "@context": "https://schema.org" }, organization));
      return;
    }

    var app = null;
    if (p.endsWith("/projects/loern.html")) {
      app = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "lœrn",
        "applicationCategory": "EducationalApplication",
        "operatingSystem": "Android, iOS",
        "isAccessibleForFree": true,
        "url": url,
        "description": description,
        "image": "https://jetztunddahanna.com/pictures/loern-icon-7d9d53a.png",
        "sameAs": [
          "https://play.google.com/store/apps/details?id=com.jetztunddahanna.loern",
          "https://apps.apple.com/app/l%C5%93rn/id6759726662"
        ],
        "author": organization
      };
    } else if (p.endsWith("/projects/sudoku.html")) {
      app = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "sudøku",
        "applicationCategory": "GameApplication",
        "operatingSystem": "Android, iOS",
        "isAccessibleForFree": true,
        "url": url,
        "description": description,
        "image": "https://jetztunddahanna.com/pictures/sudoku-icon.png",
        "sameAs": [
          "https://play.google.com/store/apps/details?id=com.jetztunddahanna.sudoku",
          "https://apps.apple.com/de/app/sud%C3%B8ku/id6793129578"
        ],
        "author": organization
      };
    }
    if (p.endsWith("/projects/tower.html")) {
      app = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "tøwer",
        "applicationCategory": "GameApplication",
        "operatingSystem": "Android",
        "isAccessibleForFree": true,
        "url": url,
        "description": description,
        "image": "https://jetztunddahanna.com/pictures/tower-icon.png",
        "sameAs": ["https://play.google.com/store/apps/details?id=com.jetztunddahanna.tower"],
        "author": organization
      };
    }
    if (app) appendJsonLd(app);
  }

  ensureAppPrivacyNoindex();
  addStructuredData();

  function updatePageTopPadding() {
    var header = document.querySelector(".site-header");
    if (!header) return;

    var headerHeight = header.offsetHeight || 0;
    var isMobile = window.matchMedia && window.matchMedia("(max-width: 768px)").matches;
    var minTop = isMobile ? 104 : 140;
    var desired = Math.max(minTop, headerHeight + 32);
    document.documentElement.style.setProperty("--page-top", desired + "px");
  }

  updatePageTopPadding();
  window.addEventListener("load", updatePageTopPadding);
  window.addEventListener("resize", updatePageTopPadding);
  window.addEventListener("orientationchange", updatePageTopPadding);
  setTimeout(updatePageTopPadding, 0);
  setTimeout(updatePageTopPadding, 250);

  function getPageKey(pathname) {
    var p = (pathname || "/").toLowerCase();
    if (p.endsWith("/about.html")) return "about";
    if (p.includes("/projects/")) return "projects";
    if (p.endsWith("/projects.html")) return "projects";
    if (p.endsWith("/principles.html")) return "principles";
    if (p.endsWith("/contact.html")) return "contact";
    return null;
  }

  function clearActive(links) {
    for (var i = 0; i < links.length; i++) {
      links[i].classList.remove("active");
      links[i].removeAttribute("aria-current");
    }
  }

  function setActiveBySuffix(links, suffix) {
    for (var i = 0; i < links.length; i++) {
      var href = links[i].getAttribute("href") || "";
      if (href.endsWith(suffix)) {
        links[i].classList.add("active");
        links[i].setAttribute("aria-current", "page");
        return;
      }
    }
  }

  var key = getPageKey(window.location.pathname);
  if (!key) return;

  var links = document.querySelectorAll(".main-nav a");
  if (!links || links.length === 0) return;

  clearActive(links);
  if (key === "about") setActiveBySuffix(links, "about.html");
  if (key === "projects") setActiveBySuffix(links, "projects.html");
  if (key === "principles") setActiveBySuffix(links, "principles.html");
  if (key === "contact") setActiveBySuffix(links, "contact.html");
})();

// Progressive enhancement: original app artwork stays available without motion,
// JavaScript, IntersectionObserver, or a successful animation-image request.
(function () {
  "use strict";
  if (!window.matchMedia || !window.IntersectionObserver) return;
  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (reducedMotion.matches) return;

  var icons = document.querySelectorAll('img[src*="pictures/loern-icon"], img[src*="pictures/sudoku-icon"], img[src*="pictures/tower-icon"]');
  if (!icons.length) return;
  var wrappers = [];
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      observer.unobserve(entry.target);
      if (reducedMotion.matches) return;
      var icon = entry.target;
      var app = /\/(loern|sudoku|tower)-icon/.exec(icon.src)[1];
      var wrapper = document.createElement("span");
      wrapper.className = "app-brand-motion";
      icon.parentNode.insertBefore(wrapper, icon);
      wrapper.appendChild(icon);
      wrappers.push(wrapper);

      var animation = new Image();
      animation.className = "app-brand-animation";
      animation.alt = "";
      animation.setAttribute("aria-hidden", "true");
      animation.onload = function () {
        if (!reducedMotion.matches && animation.parentNode === wrapper) wrapper.classList.add("is-playing");
      };
      animation.onerror = function () {
        wrapper.classList.remove("is-playing");
        animation.remove();
      };
      wrapper.appendChild(animation);
      animation.src = new URL("brand/" + app + "-splash.svg", icon.src).href;
    });
  }, { threshold: 0.35 });
  icons.forEach(function (icon) { observer.observe(icon); });

  function disableMotion(event) {
    if (!event.matches) return;
    observer.disconnect();
    wrappers.forEach(function (wrapper) {
      wrapper.classList.remove("is-playing");
      var animation = wrapper.querySelector(".app-brand-animation");
      if (animation) animation.remove();
    });
  }
  if (reducedMotion.addEventListener) reducedMotion.addEventListener("change", disableMotion);
  else if (reducedMotion.addListener) reducedMotion.addListener(disableMotion);
})();
