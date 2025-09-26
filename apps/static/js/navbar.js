// User dropdown accessibility & keyboard interactions
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.dropdown').forEach(function (drop) {
  // Support any element used as the trigger (button or anchor) which has aria-haspopup
  const btn = drop.querySelector('[aria-haspopup]');
  const menu = drop.querySelector('.dropdown-content');
    if (!btn || !menu) return;

    function close() {
      drop.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    }

    function open() {
      drop.classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
    }

    btn.addEventListener('click', function (e) {
      // If trigger is an anchor, prevent navigation
      if (btn.tagName.toLowerCase() === 'a') e.preventDefault();
      const isOpen = drop.classList.toggle('open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      if (isOpen) focusFirst();
    });

    // Make trigger keyboard-operable for links and non-button triggers
    btn.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ' || e.key === 'ArrowDown') {
        e.preventDefault();
        open();
        focusFirst();
      }
    });

    function focusFirst() {
      const first = menu.querySelector('a, button');
      if (first) first.focus();
    }

    menu.addEventListener('keydown', function (e) {
      const items = Array.from(menu.querySelectorAll('a, button'));
      const idx = items.indexOf(document.activeElement);
      if (e.key === 'Escape') {
        close();
        btn.focus();
      } else if (e.key === 'ArrowDown') {
        e.preventDefault();
  const next = (idx + 1) % items.length;
  items[next].focus();
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
  const prev = (idx - 1 + items.length) % items.length;
  items[prev].focus();
      }
    });

    // Close when clicking outside
    document.addEventListener('click', function (e) {
      if (!drop.contains(e.target)) {
        close();
      }
    });
  });
});
