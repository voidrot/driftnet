// Handles opening and closing of character scopes modals
// Accessibility: focus trap, ESC to close, ARIA attributes

document.addEventListener('DOMContentLoaded', function () {
  // Debug: confirm script loaded
  console.log('character-scopes-modal.js loaded');

  // Open modal
  document.querySelectorAll('[data-action="open-scopes-modal"]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var modalId = btn.getAttribute('data-modal-id');
      var modal = document.getElementById(modalId);
      if (modal) {
        modal.style.display = 'flex';
        modal.style.visibility = 'visible';
        modal.style.opacity = '1';
        modal.style.zIndex = '9999';
          // Also force modal-box visibility and stacking
          var modalBox = modal.querySelector('.modal-box');
          if (modalBox) {
            // Only scroll to top, do not override visibility/z-index
            modalBox.scrollTop = 0;
            modalBox.style.pointerEvents = 'auto';
            modalBox.style.visibility = 'visible';
            var overlay = modal.querySelector('.absolute.inset-0');
            if (overlay) {
              overlay.style.pointerEvents = 'none';
            }
            // Debug: print modal-box element and computed style
            console.log('Modal-box element:', modalBox);
            console.log('Modal-box computed style:', window.getComputedStyle(modalBox));
          } else {
            console.warn('Modal-box not found in modal:', modalId);
          }
        // Debug: print modal element and computed style
        console.log('Modal element:', modal);
        console.log('Modal computed style:', window.getComputedStyle(modal));
        // Focus the first focusable element in modal
        var focusable = modal.querySelector('button, [tabindex]:not([tabindex="-1"])');
        if (focusable) focusable.focus();
        // Trap focus inside modal
        trapFocus(modal);
        console.log('Opened scopes modal:', modalId);
      } else {
        console.warn('Modal not found for id:', modalId);
      }
    });
  });

  // Close modal (button or overlay)
  document.querySelectorAll('[data-action="close-scopes-modal"]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var modal = btn.closest('.modal');
      if (modal) {
        modal.style.display = 'none';
        releaseFocusTrap();
        console.log('Closed scopes modal:', modal.id);
      }
    });
  });

  // ESC key closes any open modal
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal').forEach(function (modal) {
        if (modal.style.display !== 'none') {
          modal.style.display = 'none';
          releaseFocusTrap();
          console.log('Closed modal via ESC:', modal.id);
        }
      });
    }
  });

  // Focus trap helpers
  let lastFocusedElement = null;
  function trapFocus(modal) {
    lastFocusedElement = document.activeElement;
    modal.addEventListener('keydown', focusHandler);
  }
  function releaseFocusTrap() {
    document.removeEventListener('keydown', focusHandler);
    if (lastFocusedElement) lastFocusedElement.focus();
    lastFocusedElement = null;
  }
  function focusHandler(e) {
    if (e.key !== 'Tab') return;
    const focusableEls = Array.from(e.currentTarget.querySelectorAll('button, [tabindex]:not([tabindex="-1"])'));
    if (!focusableEls.length) return;
    const first = focusableEls[0];
    const last = focusableEls[focusableEls.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      last.focus();
      e.preventDefault();
    } else if (!e.shiftKey && document.activeElement === last) {
      first.focus();
      e.preventDefault();
    }
  }
});
