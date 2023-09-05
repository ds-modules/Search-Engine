const image2 = document.getElementById('image2');
const modal2 = document.getElementById('myModal2');
const overlay2 = document.getElementById('overlay2');
const closeModal2 = document.getElementById('closeModal2');

image2.addEventListener('click', () => {
  modal2.style.display = 'block';
  overlay2.style.display = 'block';
});

closeModal2.addEventListener('click', () => {
  modal2.style.display = 'none';
  overlay2.style.display = 'none';
});