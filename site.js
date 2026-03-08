(function () {
  "use strict";

  function updatePageTopPadding() {
    var header = document.querySelector(".site-header");
    if (!header) return;

    // Ensure content never sits under the fixed header.
    // Keep the existing spacing as a minimum (smaller on mobile).
    var headerHeight = header.offsetHeight || 0;
    var isMobile = window.matchMedia && window.matchMedia("(max-width: 768px)").matches;
    var minTop = isMobile ? 110 : 160;
    var desired = Math.max(minTop, headerHeight + 24);
    document.documentElement.style.setProperty("--page-top", desired + "px");
  }

  // site.js is loaded at the end of <body>, but header height can change
  // after layout/paint (e.g. wrapping, fonts). Update a few times.
  updatePageTopPadding();
  window.addEventListener("load", updatePageTopPadding);
  window.addEventListener("resize", updatePageTopPadding);
  window.addEventListener("orientationchange", updatePageTopPadding);
  setTimeout(updatePageTopPadding, 0);
  setTimeout(updatePageTopPadding, 250);

  function getPageKey(pathname) {
    // Normalize
    var p = (pathname || "/").toLowerCase();

    if (p.endsWith("/about.html")) return "about";
    if (p.includes("/projects/")) return "projects";
    if (p.endsWith("/projects.html")) return "projects";
    if (p.endsWith("/principles.html")) return "principles";
    if (p.endsWith("/contact.html")) return "contact";

    // Default: no active link for home/legal/other pages
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
