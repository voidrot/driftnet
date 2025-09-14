// apps/static/js/character-delete-modal.js
document.addEventListener('DOMContentLoaded', function () {
  // Attach open modal listeners
  document.querySelectorAll('[data-action="open-delete-modal"]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      // Find the closest modal in the DOM tree (since modal is per card)
      const card = btn.closest('.card');
      if (!card) return;
      const modal = card.querySelector('#deleteModal');
      if (!modal) return;
      const form = modal.querySelector('#deleteModalForm');
      const text = modal.querySelector('#deleteModalText');
      const characterId = btn.getAttribute('data-character-id');
      const characterName = btn.getAttribute('data-character-name');
      text.textContent = `Are you sure you want to delete ${characterName}?`;
      // Use the data-delete-url attribute for deletion
      const deleteUrl = btn.getAttribute('data-delete-url');
      if (deleteUrl) {
        form.action = deleteUrl;
      }
      // Set both character_id and token_id hidden fields
      modal.querySelector('#deleteModalCharacterId').value = characterId;
      const tokenId = btn.getAttribute('data-token-id');
      const tokenInput = modal.querySelector('#deleteModalTokenId');
      if (tokenInput && tokenId) {
        tokenInput.value = tokenId;
      }
      modal.style.display = 'flex';
      modal.classList.add('modal-open');
      // Accessibility: focus the first button in the modal
      setTimeout(() => {
        const firstBtn = modal.querySelector('button, [tabindex="0"]');
        if (firstBtn) firstBtn.focus();
      }, 50);
    });
  });

  // Attach close modal listeners (cancel button and backdrop)
  document.querySelectorAll('[data-action="close-delete-modal"]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      // Find the closest modal in the DOM tree
      const modal = btn.closest('#deleteModal');
      if (!modal) return;
      modal.style.display = 'none';
      modal.classList.remove('modal-open');
      // Accessibility: return focus to the delete button
      const card = modal.closest('.card');
      if (card) {
        const deleteBtn = card.querySelector('[data-action="open-delete-modal"]');
        if (deleteBtn) deleteBtn.focus();
      }
    });
  });
});
