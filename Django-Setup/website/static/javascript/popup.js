const image = document.getElementById('image');
const modal = document.getElementById('myModal');
const overlay = document.getElementById('overlay');
const closeModal = document.getElementById('closeModal');

image.addEventListener('click', () => {
  modal.style.display = 'block';
  overlay.style.display = 'block';
});

closeModal.addEventListener('click', () => {
  modal.style.display = 'none';
  overlay.style.display = 'none';
});

