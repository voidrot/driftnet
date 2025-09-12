// apps/static/js/character-delete-modal.js
function openDeleteModal(characterId, characterName) {
  const modal = document.getElementById('deleteModal');
  const form = document.getElementById('deleteModalForm');
  const text = document.getElementById('deleteModalText');
  text.textContent = `Are you sure you want to delete ${characterName}?`;
  // Use the named URL pattern for deletion
  const url = window.deleteModalDeleteUrl.replace('/0/', `/${characterId}/`);
  form.action = url;
  document.getElementById('deleteModalCharacterId').value = characterId;
  modal.style.display = 'flex';
  modal.classList.add('modal-open');
}
function closeDeleteModal() {
  const modal = document.getElementById('deleteModal');
  modal.style.display = 'none';
  modal.classList.remove('modal-open');
}
