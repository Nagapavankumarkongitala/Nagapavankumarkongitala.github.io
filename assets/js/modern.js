/* ==========================================================================
   Lightweight, dependency-free enhancements.
   Every content element is visible and usable without this file.
   ========================================================================== */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function ready(callback) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", callback, { once: true });
    } else {
      callback();
    }
  }

  /* ---------- Preloader ---------- */
  function dismissPreloader() {
    var preloader = document.querySelector(".preloader");
    if (!preloader) return;
    preloader.classList.add("is-hidden");
    window.setTimeout(function () {
      if (preloader.parentNode) preloader.parentNode.removeChild(preloader);
    }, reduceMotion ? 0 : 320);
  }

  /* ---------- Mobile navigation ---------- */
  function initNavigation() {
    var toggler = document.querySelector(".navbar-toggler");
    var collapse = document.getElementById("navbarCollapse");
    if (!toggler || !collapse) return;

    toggler.addEventListener("click", function () {
      var open = collapse.classList.toggle("show");
      toggler.setAttribute("aria-expanded", String(open));
    });

    collapse.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        collapse.classList.remove("show");
        toggler.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---------- Portfolio filters ---------- */
  function initFilters() {
    var grid = document.getElementById("portfolio-grid");
    var filters = Array.prototype.slice.call(document.querySelectorAll(".controls .filter"));
    if (!grid || !filters.length) return;

    grid.classList.add("js-filter");
    var cards = Array.prototype.slice.call(grid.querySelectorAll(".mix"));

    function applyFilter(button) {
      var value = button.getAttribute("data-filter") || "all";

      filters.forEach(function (item) {
        var active = item === button;
        item.classList.toggle("active", active);
        item.setAttribute("aria-pressed", String(active));
      });

      cards.forEach(function (card) {
        var show = value === "all" || card.classList.contains(value.replace(/^\./, ""));
        card.classList.toggle("is-visible", show);
      });
    }

    filters.forEach(function (button) {
      button.addEventListener("click", function () { applyFilter(button); });
    });

    applyFilter(filters[0]);
  }

  /* ---------- Reveal on scroll ---------- */
  function initReveals() {
    if (reduceMotion || !("IntersectionObserver" in window)) return;
    document.documentElement.classList.add("js-motion");

    var targets = Array.prototype.slice.call(
      document.querySelectorAll(".wow, .ftco-animate, .reveal")
    );
    if (!targets.length) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-revealed");
        observer.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });

    targets.forEach(function (target) { observer.observe(target); });
  }

  /* ---------- Active navigation + scroll affordances ---------- */
  function initScrollUi() {
    var nav = document.querySelector(".site-navigation");
    var top = document.querySelector(".back-to-top");
    var links = Array.prototype.slice.call(document.querySelectorAll(".nav-link[href^='#']"));

    function onScroll() {
      var offset = window.pageYOffset || document.documentElement.scrollTop;
      if (nav) nav.classList.toggle("navbar-fixed", offset > 100);
      if (top) top.classList.toggle("is-visible", offset > 200);
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    if (top) {
      top.addEventListener("click", function (event) {
        event.preventDefault();
        window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
      });
    }

    if (!("IntersectionObserver" in window) || !links.length) return;

    var byId = {};
    links.forEach(function (link) {
      var id = link.getAttribute("href").slice(1);
      if (id && document.getElementById(id)) byId[id] = link;
    });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (link) {
          link.classList.remove("active");
          link.removeAttribute("aria-current");
        });
        var link = byId[entry.target.id];
        if (link) {
          link.classList.add("active");
          link.setAttribute("aria-current", "true");
        }
      });
    }, { rootMargin: "-35% 0px -55% 0px", threshold: 0 });

    Object.keys(byId).forEach(function (id) {
      observer.observe(document.getElementById(id));
    });
  }

  ready(function () {
    dismissPreloader();
    initNavigation();
    initFilters();
    initReveals();
    initScrollUi();
  });
})();
