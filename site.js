(function () {
  "use strict";

  var SEO_LOCALES = [
    { path: "de", hreflang: "de" },
    { path: "en", hreflang: "en" },
    { path: "fr", hreflang: "fr" },
    { path: "es", hreflang: "es" },
    { path: "it", hreflang: "it" },
    { path: "nl", hreflang: "nl" },
    { path: "sv", hreflang: "sv" },
    { path: "pl", hreflang: "pl" },
    { path: "pt-br", hreflang: "pt-BR" },
    { path: "pt-pt", hreflang: "pt-PT" }
  ];

  function getLocalizedRelativePath(pathname) {
    var parts = (pathname || "/").split("/").filter(Boolean);
    if (!parts.length) return null;
    var localeFound = false;
    for (var i = 0; i < SEO_LOCALES.length; i++) {
      if (SEO_LOCALES[i].path === parts[0].toLowerCase()) {
        localeFound = true;
        break;
      }
    }
    if (!localeFound) return null;
    return parts.slice(1).join("/");
  }

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

  function addHreflangLinks() {
    var relativePath = getLocalizedRelativePath(window.location.pathname);
    if (relativePath === null) return;
    var supported = {
      "": true,
      "about.html": true,
      "contact.html": true,
      "principles.html": true,
      "projects.html": true,
      "projects/loern.html": true,
      "projects/sudoku.html": true
    };
    if (!supported[relativePath]) return;

    var base = "https://jetztunddahanna.com/";
    for (var i = 0; i < SEO_LOCALES.length; i++) {
      var locale = SEO_LOCALES[i];
      var link = document.createElement("link");
      link.rel = "alternate";
      link.hreflang = locale.hreflang;
      link.href = base + locale.path + "/" + relativePath;
      document.head.appendChild(link);
    }
    var fallback = document.createElement("link");
    fallback.rel = "alternate";
    fallback.hreflang = "x-default";
    fallback.href = base + "en/" + relativePath;
    document.head.appendChild(fallback);
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
        "image": "https://jetztunddahanna.com/Loern_full_white.png",
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
        "image": "https://jetztunddahanna.com/pictures/icon.png",
        "sameAs": [
          "https://play.google.com/store/apps/details?id=com.jetztunddahanna.sudoku",
          "https://apps.apple.com/de/app/sud%C3%B8ku/id6793129578"
        ],
        "author": organization
      };
    }
    if (app) appendJsonLd(app);
  }

  ensureAppPrivacyNoindex();
  addHreflangLinks();
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
