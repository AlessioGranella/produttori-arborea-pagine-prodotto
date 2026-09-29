/* Comportamenti comuni a tutte le pagine: menu, sottomenu, torna su. */
(function () {
  'use strict';

  /* ---------------------------------------------------------- burger */
  var burger = document.querySelector('.pa-burger');
  var nav = document.getElementById('menu-principale');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var aperto = nav.getAttribute('data-aperto') === 'true';
      nav.setAttribute('data-aperto', String(!aperto));
      burger.setAttribute('aria-expanded', String(!aperto));
    });
  }

  /* -------------------------------------------------------- sottomenu */
  var voci = Array.prototype.slice.call(document.querySelectorAll('.pa-nav__item'));

  function chiudiTutti(tranne) {
    voci.forEach(function (v) {
      if (v === tranne) return;
      v.setAttribute('data-open', 'false');
      var t = v.querySelector('.pa-nav__toggle');
      if (t) t.setAttribute('aria-expanded', 'false');
    });
  }

  voci.forEach(function (voce) {
    var toggle = voce.querySelector('.pa-nav__toggle');
    if (!toggle) return;

    toggle.addEventListener('click', function (e) {
      e.preventDefault();
      var aperto = voce.getAttribute('data-open') === 'true';
      chiudiTutti(voce);
      voce.setAttribute('data-open', String(!aperto));
      toggle.setAttribute('aria-expanded', String(!aperto));
    });

    // su desktop il sottomenu si apre anche al passaggio del mouse
    voce.addEventListener('mouseenter', function () {
      if (window.matchMedia('(min-width:1025px)').matches) {
        chiudiTutti(voce);
        voce.setAttribute('data-open', 'true');
        toggle.setAttribute('aria-expanded', 'true');
      }
    });
    voce.addEventListener('mouseleave', function () {
      if (window.matchMedia('(min-width:1025px)').matches) {
        voce.setAttribute('data-open', 'false');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  });

  document.addEventListener('click', function (e) {
    if (!e.target.closest('.pa-nav') && !e.target.closest('.pa-burger')) chiudiTutti(null);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') chiudiTutti(null);
  });

  /* -------------------------------------------------------- torna su */
  var su = document.querySelector('.pa-su');
  if (su) {
    su.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    var aggiorna = function () {
      su.setAttribute('data-visibile', String(window.scrollY > 700));
    };
    window.addEventListener('scroll', aggiorna, { passive: true });
    aggiorna();
  }
})();
