// Modal logic for Show Scopes and Add Character button
(function() {
  const toggleBtn = document.getElementById('toggleScopesBtn');
  const scopesModal = document.getElementById('scopesModal');
  const closeModalBtn = document.getElementById('closeScopesModalBtn');
  const addCharacterBtn = document.getElementById('addCharacterBtn');
  let lastFocusedElement = null;
  if (!toggleBtn || !scopesModal || !closeModalBtn) return;
  function openScopesModal() {
    lastFocusedElement = document.activeElement;
    scopesModal.style.display = 'flex';
    toggleBtn.setAttribute('aria-expanded', true);
    setTimeout(() => {
      const firstInput = scopesModal.querySelector('input[type="checkbox"]');
      if (firstInput) firstInput.focus();
      else closeModalBtn.focus();
    }, 0);
  }
  function closeScopesModal() {
    scopesModal.style.display = 'none';
    toggleBtn.setAttribute('aria-expanded', false);
    toggleBtn.querySelector('h3').textContent = 'Show Scopes';
    if (lastFocusedElement) lastFocusedElement.focus();
  }
  toggleBtn.addEventListener('click', function(e) {
    openScopesModal();
    toggleBtn.querySelector('h3').textContent = 'Hide Scopes';
  });
  closeModalBtn.addEventListener('click', closeScopesModal);
  scopesModal.addEventListener('mousedown', function(e) {
    if (e.target === scopesModal) closeScopesModal();
  });
  document.addEventListener('keydown', function(e) {
    if (scopesModal.style.display === 'flex') {
      if (e.key === 'Escape') closeScopesModal();
      // Basic focus trap
      if (e.key === 'Tab') {
        const focusable = scopesModal.querySelectorAll('input,button,[tabindex]:not([tabindex="-1"])');
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    }
  });

  // Add Character button logic
  if (addCharacterBtn) {
    addCharacterBtn.addEventListener('click', function() {
      // Only collect checked scopes from the modal
      const modal = document.getElementById('scopesModal');
      const checked = modal ? modal.querySelectorAll('input[name="scopes"]:checked') : [];
      const scopes = Array.from(checked).map(cb => cb.value);
      const baseUrl = addCharacterBtn.getAttribute('data-redirect-url');
      const returnUrl = addCharacterBtn.getAttribute('data-return-url');
      const url = new URL(baseUrl, window.location.origin);
      // Always send scopes param (empty string if none)
      url.searchParams.set('scopes', scopes.join(' '));
      if (returnUrl) {
        url.searchParams.set('return_to', returnUrl);
      }
      window.location.href = url.toString();
    });
  }
})();
