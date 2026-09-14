(function () {
  'use strict';

  /* theme toggle -------------------------------------------------- */
  var btn = document.getElementById('theme-toggle');
  if (btn) {
    btn.addEventListener('click', function () {
      var root = document.documentElement;
      var cur = root.getAttribute('data-theme');
      if (!cur) {
        cur = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      }
      var next = cur === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  }

  /* lesson filter on the index ------------------------------------ */
  var filter = document.getElementById('filter');
  if (filter) {
    var rows = Array.prototype.slice.call(document.querySelectorAll('#rows li'));
    var none = document.getElementById('noresult');
    filter.addEventListener('input', function () {
      var q = filter.value.trim().toLowerCase();
      var shown = 0;
      rows.forEach(function (r) {
        var hit = !q || r.getAttribute('data-search').indexOf(q) !== -1;
        r.hidden = !hit;
        if (hit) shown++;
      });
      if (none) none.hidden = shown !== 0;
    });
  }

  /* wide tables get their own scroll container -------------------- */
  Array.prototype.forEach.call(document.querySelectorAll('.passage table'), function (t) {
    if (t.parentNode.classList.contains('tablewrap')) return;
    var w = document.createElement('div');
    w.className = 'tablewrap';
    t.parentNode.insertBefore(w, t);
    w.appendChild(t);
  });

  /* left / right arrows move between lessons ---------------------- */
  document.addEventListener('keydown', function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var tag = (e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || e.target.isContentEditable) return;
    var sel = e.key === 'ArrowLeft' ? '.pn.prev a' : e.key === 'ArrowRight' ? '.pn.next a' : null;
    if (!sel) return;
    var link = document.querySelector(sel);
    if (link && link.href) window.location.href = link.href;
  });
})();
