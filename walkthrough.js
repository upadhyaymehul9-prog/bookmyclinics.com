/**
 * BookMyClinic — Dynamic Walkthrough
 * Add this script at the bottom of index.html on bookmyclinics.com
 * Shows once per user, never again after completion or skip
 */
(function () {
  'use strict';

  // Already seen? Exit immediately
  try { if (localStorage.getItem('bmc_tour_done')) return; } catch (e) { return; }

  var steps = [
    {
      targetId:  null,
      position:  'center',
      emoji:     '👋',
      title:     'Welcome to BookMyClinic!',
      desc:      'Let us show you around in 4 quick steps. Takes less than a minute.',
      btnLabel:  'Start Tour →'
    },
    {
      targetSelector: 'a[href="#book"].btn-primary, a.btn-primary',
      position:       'bottom',
      emoji:          '🏥',
      title:          'Book an Appointment',
      desc:           'Tap here to browse all clinics near you and reserve a slot instantly — no account needed.',
      btnLabel:       'Next →'
    },
    {
      targetSelector: 'a[href="#register"].btn-secondary, a[href="#register"]',
      position:       'bottom',
      emoji:          '🩺',
      title:          'Register Your Clinic',
      desc:           'Are you a doctor? Join as a Founding Partner — completely free forever. 5 minutes to set up.',
      btnLabel:       'Next →'
    },
    {
      targetSelector: '.stats-bar, .stats-inner',
      position:       'bottom',
      emoji:          '✅',
      title:          'Why BookMyClinic?',
      desc:           'Available 24x7. Zero OTP. Zero registration. Zero cost for patients. Everything patients need.',
      btnLabel:       'Next →'
    },
    {
      targetSelector: '#how',
      position:       'top',
      emoji:          '🚀',
      title:          'Up and running in 4 steps',
      desc:           'Register free → Add doctors → Share link → Go live 24x7. Patients book, you get WhatsApp confirmation.',
      btnLabel:       "Let's Go! 🎉"
    }
  ];

  var current = 0;

  /* ── STYLES ── */
  var style = document.createElement('style');
  style.textContent = [
    '@import url("https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&display=swap");',

    '.bmc-overlay {',
    '  position: fixed; inset: 0; z-index: 99998;',
    '  pointer-events: none;',
    '  transition: opacity 0.3s;',
    '}',

    '.bmc-backdrop {',
    '  position: fixed; inset: 0; z-index: 99997;',
    '  background: rgba(5,13,26,0.82);',
    '  backdrop-filter: blur(3px);',
    '  pointer-events: all;',
    '  transition: opacity 0.4s;',
    '}',

    '.bmc-spotlight {',
    '  position: fixed; z-index: 99999;',
    '  border-radius: 14px;',
    '  box-shadow: 0 0 0 9999px rgba(5,13,26,0.82), 0 0 0 3px rgba(56,189,248,0.6), 0 0 40px rgba(37,99,235,0.4);',
    '  pointer-events: none;',
    '  transition: all 0.45s cubic-bezier(0.4,0,0.2,1);',
    '  background: transparent;',
    '}',

    '.bmc-tooltip {',
    '  position: fixed; z-index: 100000;',
    '  background: #0c1829;',
    '  border: 1.5px solid rgba(56,189,248,0.3);',
    '  border-radius: 20px;',
    '  padding: 20px 22px 18px;',
    '  width: min(320px, calc(100vw - 32px));',
    '  box-shadow: 0 16px 48px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.04);',
    '  font-family: "Outfit", sans-serif;',
    '  transition: all 0.35s cubic-bezier(0.4,0,0.2,1);',
    '  pointer-events: all;',
    '}',

    '.bmc-tooltip-emoji {',
    '  font-size: 32px; margin-bottom: 10px; display: block;',
    '  animation: bmc-bounce 1.5s ease-in-out infinite alternate;',
    '}',
    '@keyframes bmc-bounce {',
    '  from { transform: translateY(0); }',
    '  to   { transform: translateY(-6px); }',
    '}',

    '.bmc-tooltip-title {',
    '  font-size: 17px; font-weight: 800; color: #fff;',
    '  letter-spacing: -0.4px; margin-bottom: 8px; line-height: 1.2;',
    '}',

    '.bmc-tooltip-desc {',
    '  font-size: 13px; color: rgba(255,255,255,0.55);',
    '  line-height: 1.65; margin-bottom: 18px;',
    '}',

    '.bmc-tooltip-footer {',
    '  display: flex; align-items: center; justify-content: space-between; gap: 10px;',
    '}',

    '.bmc-dots {',
    '  display: flex; gap: 5px; align-items: center;',
    '}',
    '.bmc-dot {',
    '  width: 6px; height: 6px; border-radius: 3px;',
    '  background: rgba(255,255,255,0.2);',
    '  transition: all 0.3s;',
    '}',
    '.bmc-dot.active {',
    '  width: 20px;',
    '  background: linear-gradient(90deg, #2563eb, #38bdf8);',
    '}',

    '.bmc-next-btn {',
    '  background: linear-gradient(135deg, #2563eb, #38bdf8);',
    '  border: none; border-radius: 12px;',
    '  padding: 10px 20px;',
    '  font-family: "Outfit", sans-serif;',
    '  font-size: 13px; font-weight: 700; color: #fff;',
    '  cursor: pointer;',
    '  box-shadow: 0 4px 16px rgba(37,99,235,0.4);',
    '  transition: transform 0.15s, box-shadow 0.15s;',
    '  white-space: nowrap;',
    '}',
    '.bmc-next-btn:hover { transform: translateY(-1px); box-shadow: 0 6px 20px rgba(37,99,235,0.55); }',
    '.bmc-next-btn:active { transform: scale(0.96); }',

    '.bmc-skip {',
    '  font-size: 11px; color: rgba(255,255,255,0.25);',
    '  cursor: pointer; background: none; border: none;',
    '  font-family: "Outfit", sans-serif;',
    '  padding: 4px 0;',
    '  transition: color 0.2s;',
    '}',
    '.bmc-skip:hover { color: rgba(255,255,255,0.5); }',

    '.bmc-progress-bar {',
    '  height: 2px;',
    '  background: rgba(255,255,255,0.07);',
    '  border-radius: 1px;',
    '  margin-bottom: 16px;',
    '  overflow: hidden;',
    '}',
    '.bmc-progress-fill {',
    '  height: 100%;',
    '  background: linear-gradient(90deg, #2563eb, #2dd4bf);',
    '  border-radius: 1px;',
    '  transition: width 0.4s ease;',
    '}'
  ].join('\n');
  document.head.appendChild(style);

  /* ── DOM ── */
  var backdrop  = document.createElement('div');
  backdrop.className = 'bmc-backdrop';
  document.body.appendChild(backdrop);

  var spotlight = document.createElement('div');
  spotlight.className = 'bmc-spotlight';
  document.body.appendChild(spotlight);

  var tooltip = document.createElement('div');
  tooltip.className = 'bmc-tooltip';
  document.body.appendChild(tooltip);

  /* ── HELPERS ── */
  function getTarget(step) {
    if (!step.targetSelector) return null;
    return document.querySelector(step.targetSelector);
  }

  function getDots(currentIdx, total) {
    var html = '<div class="bmc-dots">';
    for (var i = 0; i < total; i++) {
      html += '<div class="bmc-dot' + (i === currentIdx ? ' active' : '') + '"></div>';
    }
    html += '</div>';
    return html;
  }

  function positionTooltip(targetEl, position) {
    var tt  = tooltip;
    var rect = targetEl ? targetEl.getBoundingClientRect() : null;
    var vw  = window.innerWidth;
    var vh  = window.innerHeight;
    var ttW = 320;
    var ttH = tooltip.offsetHeight || 200;
    var pad = 16;

    if (!rect || position === 'center') {
      // Center of screen
      tt.style.top  = Math.round((vh - ttH) / 2) + 'px';
      tt.style.left = Math.round((vw - Math.min(ttW, vw - 32)) / 2) + 'px';
      return;
    }

    var left = Math.round(rect.left + rect.width / 2 - Math.min(ttW, vw - 32) / 2);
    left = Math.max(pad, Math.min(left, vw - Math.min(ttW, vw - 32) - pad));

    var top;
    if (position === 'bottom') {
      top = Math.round(rect.bottom + 16);
      if (top + ttH > vh - pad) top = Math.round(rect.top - ttH - 16);
    } else {
      top = Math.round(rect.top - ttH - 16);
      if (top < pad) top = Math.round(rect.bottom + 16);
    }
    top = Math.max(pad, Math.min(top, vh - ttH - pad));

    tt.style.top  = top + 'px';
    tt.style.left = left + 'px';
  }

  function scrollToTarget(el, callback) {
    if (!el) { callback(); return; }
    var rect = el.getBoundingClientRect();
    var pad  = 100;
    var inView = rect.top >= pad && rect.bottom <= window.innerHeight - pad;
    if (inView) { callback(); return; }
    var targetY = window.scrollY + rect.top - window.innerHeight / 2 + rect.height / 2;
    window.scrollTo({ top: targetY, behavior: 'smooth' });
    setTimeout(callback, 500);
  }

  function renderStep(idx) {
    var step   = steps[idx];
    var target = getTarget(step);
    var total  = steps.length;
    var progressPct = Math.round((idx / (total - 1)) * 100);

    // Scroll target into view first
    scrollToTarget(target, function () {

      // Update spotlight
      if (target) {
        var r   = target.getBoundingClientRect();
        var pad = 8;
        spotlight.style.display = 'block';
        spotlight.style.left    = (r.left - pad) + 'px';
        spotlight.style.top     = (r.top  - pad) + 'px';
        spotlight.style.width   = (r.width  + pad * 2) + 'px';
        spotlight.style.height  = (r.height + pad * 2) + 'px';
      } else {
        spotlight.style.display = 'none';
      }

      // Build tooltip HTML
      var isLast = idx === total - 1;
      tooltip.innerHTML =
        '<div class="bmc-progress-bar"><div class="bmc-progress-fill" style="width:' + progressPct + '%"></div></div>' +
        '<span class="bmc-tooltip-emoji">' + step.emoji + '</span>' +
        '<div class="bmc-tooltip-title">' + step.title + '</div>' +
        '<div class="bmc-tooltip-desc">'  + step.desc  + '</div>' +
        '<div class="bmc-tooltip-footer">' +
          getDots(idx, total) +
          '<div style="display:flex;gap:10px;align-items:center;">' +
            (idx > 0 && !isLast ? '<button class="bmc-skip" id="bmcSkip">Skip</button>' : '') +
            '<button class="bmc-next-btn" id="bmcNext">' + step.btnLabel + '</button>' +
          '</div>' +
        '</div>';

      // Position tooltip
      positionTooltip(target, step.position);

      // Wire buttons
      var nextBtn  = document.getElementById('bmcNext');
      var skipBtn  = document.getElementById('bmcSkip');
      if (nextBtn) nextBtn.addEventListener('click', function () {
        if (idx < total - 1) { current++; renderStep(current); }
        else finish();
      });
      if (skipBtn) skipBtn.addEventListener('click', finish);
    });
  }

  function finish() {
    try { localStorage.setItem('bmc_tour_done', '1'); } catch (e) {}
    backdrop.style.opacity  = '0';
    tooltip.style.opacity   = '0';
    spotlight.style.opacity = '0';
    setTimeout(function () {
      backdrop.remove();
      tooltip.remove();
      spotlight.remove();
    }, 400);
  }

  // Reposition on resize/scroll
  window.addEventListener('resize', function () {
    if (current < steps.length) renderStep(current);
  });

  // Kick off after short delay to let page render
  setTimeout(function () { renderStep(0); }, 800);

})();
