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

setTimeout(function() {
  document.querySelector(".i1").classList.add("zoom-in"); /* add the class to start the animation */
}, 3000);


function scrollToHalf() {
  // Calculate the halfway point of the page
  const halfwayPoint = document.documentElement.scrollHeight / 4.5;

  // Scroll to the halfway point of the page
  document.documentElement.scrollTop = halfwayPoint;
  document.body.scrollTop = halfwayPoint;
}

function scrollToBottom() {
  // Calculate the halfway point of the page
  const bottomPoint = document.documentElement.scrollHeight / 1.8;

  // Scroll to the halfway point of the page
  document.documentElement.scrollTop = bottomPoint;
  document.body.scrollTop = bottomPoint;
}