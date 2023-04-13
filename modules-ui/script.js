const slideInText2 = document.querySelector('.slide-in-text2');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('slide-in2');
    } else {
      entry.target.classList.remove('slide-in2');
    }
  });
});

observer.observe(slideInText2);
