/* LAVO landing page behaviour.
   Coverage areas come from Django via the #coverage-data JSON block, so
   landing/content.py stays the single source of truth. */
(function () {
  "use strict";

  /* ---------- mobile menu ---------- */
  var burger = document.getElementById('burger');
  var drawer = document.getElementById('drawer');
  if (burger && drawer) {
    burger.addEventListener('click', function () {
      var open = drawer.hidden;
      drawer.hidden = !open;
      burger.setAttribute('aria-expanded', String(open));
    });
    drawer.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        drawer.hidden = true;
        burger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---------- Home dropdown ---------- */
  var homeBtn = document.getElementById('homeBtn');
  var homeMenu = document.getElementById('homeMenu');
  if (homeBtn && homeMenu) {
    var closeHome = function () {
      homeMenu.hidden = true;
      homeBtn.setAttribute('aria-expanded', 'false');
    };
    homeBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = homeMenu.hidden;
      homeMenu.hidden = !open;
      homeBtn.setAttribute('aria-expanded', String(open));
    });
    homeMenu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') closeHome();
    });
    document.addEventListener('click', function (e) {
      if (!homeMenu.hidden && !homeMenu.contains(e.target) && e.target !== homeBtn) closeHome();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !homeMenu.hidden) {
        closeHome();
        homeBtn.focus();
      }
    });
  }

  /* ---------- coverage checker + map ---------- */
  var dataEl = document.getElementById('coverage-data');
  var svgMap = document.getElementById('covmap');
  var form = document.getElementById('coverForm');
  if (!dataEl || !svgMap || !form) return;

  var AREAS = JSON.parse(dataEl.textContent);
  var PHONE_DISPLAY = '0993 921 6705';
  var PHONE_TEL = '+639939216705';

  var msg = document.getElementById('coverMsg');
  var gmapsBtn = document.getElementById('gmapsBtn');
  var zoomIn = document.getElementById('zoomIn');
  var zoomOut = document.getElementById('zoomOut');
  var input = document.getElementById('areaInput');
  var pins = Array.prototype.slice.call(document.querySelectorAll('.covmap .marker'));

  var BASE = { x: 0, y: 0, w: 600, h: 400 };
  var MAXZ = 3;
  var view = { x: BASE.x, y: BASE.y, w: BASE.w, h: BASE.h };
  var zoom = 0;
  var focusPt = { x: BASE.w / 2, y: BASE.h / 2 };
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var raf = null;
  var DEFAULT_MSG = msg.innerHTML;

  function gmapsUrl(query) {
    return 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(query);
  }

  function phoneLink() {
    return '<a href="tel:' + PHONE_TEL + '">' + PHONE_DISPLAY + '</a>';
  }

  function targetView() {
    var k = Math.pow(0.66, zoom);
    var w = BASE.w * k;
    var h = BASE.h * k;
    return {
      x: Math.max(BASE.x, Math.min(BASE.x + BASE.w - w, focusPt.x - w / 2)),
      y: Math.max(BASE.y, Math.min(BASE.y + BASE.h - h, focusPt.y - h / 2)),
      w: w,
      h: h
    };
  }

  function paintView(v) {
    svgMap.setAttribute('viewBox',
      v.x.toFixed(1) + ' ' + v.y.toFixed(1) + ' ' + v.w.toFixed(1) + ' ' + v.h.toFixed(1));
  }

  function syncZoom() {
    zoomIn.disabled = zoom >= MAXZ;
    zoomOut.disabled = zoom <= 0;
  }

  function flyTo() {
    var to = targetView();
    syncZoom();
    if (raf) cancelAnimationFrame(raf);
    if (reduceMotion) {
      view = to;
      paintView(view);
      return;
    }
    var from = { x: view.x, y: view.y, w: view.w, h: view.h };
    var t0 = performance.now();
    (function step(now) {
      var p = Math.min(1, (now - t0) / 180);
      var e = p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
      view = {
        x: from.x + (to.x - from.x) * e,
        y: from.y + (to.y - from.y) * e,
        w: from.w + (to.w - from.w) * e,
        h: from.h + (to.h - from.h) * e
      };
      paintView(view);
      if (p < 1) raf = requestAnimationFrame(step);
    })(performance.now());
  }

  function resetView() {
    zoom = 0;
    focusPt = { x: BASE.w / 2, y: BASE.h / 2 };
    flyTo();
  }

  zoomIn.addEventListener('click', function () {
    if (zoom < MAXZ) { zoom++; flyTo(); }
  });
  zoomOut.addEventListener('click', function () {
    if (zoom > 0) { zoom--; if (zoom === 0) focusPt = { x: BASE.w / 2, y: BASE.h / 2 }; flyTo(); }
  });

  function highlight(id) {
    var found = null;
    pins.forEach(function (p) {
      var on = p.getAttribute('data-id') === id;
      p.classList.toggle('hit', on);
      if (on) found = p;
    });
    if (found) {
      focusPt = { x: Number(found.getAttribute('data-cx')), y: Number(found.getAttribute('data-cy')) };
      if (zoom < 2) zoom = 2;
      flyTo();
    }
  }

  /* longest matching keyword wins, so "parkhomes tunasan" beats "tunasan" */
  function matchArea(q) {
    var best = null;
    var len = 0;
    AREAS.forEach(function (a) {
      a.keys.forEach(function (k) {
        if (q.indexOf(k) > -1 && k.length > len) { best = a; len = k.length; }
      });
    });
    return best;
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var raw = (input.value || '').trim();
    if (!raw) {
      highlight(null);
      msg.innerHTML = DEFAULT_MSG;
      resetView();
      return;
    }
    var area = matchArea(raw.toLowerCase());
    if (area) {
      highlight(area.id);
      gmapsBtn.href = gmapsUrl(area.query);
      msg.innerHTML = '<b>Yes — we pick up in ' + area.label + '.</b> It’s marked on the map. Call '
        + phoneLink() + ' to book your pickup.';
    } else {
      highlight(null);
      gmapsBtn.href = gmapsUrl(raw + ', Philippines');
      resetView();
      msg.innerHTML = '<b>Let’s check that one.</b> It isn’t on our regular route, but we cater to '
        + 'other areas. Send your complete address to ' + phoneLink() + ' and we’ll confirm.';
    }
  });

  function selectPin(p) {
    var id = p.getAttribute('data-id');
    var area = AREAS.filter(function (a) { return a.id === id; })[0];
    if (!area) return;
    input.value = area.label;
    highlight(area.id);
    gmapsBtn.href = gmapsUrl(area.query);
    msg.innerHTML = '<b>Yes — we pick up in ' + area.label + '.</b> Call '
      + phoneLink() + ' to book your pickup.';
  }

  pins.forEach(function (p) {
    p.addEventListener('click', function () { selectPin(p); });
    p.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); selectPin(p); }
    });
  });
})();
