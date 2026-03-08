(function () {
  "use strict";

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
