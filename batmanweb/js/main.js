let slideIndex = 1;
showSlides(slideIndex);


function plusSlides(n) {
  showSlides(slideIndex += n);
}


function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
function showHamburger(){
  const sidebar = document.querySelector('.hamb')
  sidebar.style.display = 'flex'
  const navbar = document.querySelector('.hideondesk')
  navbar.style.display = 'none'
  const hambutton = document.querySelector('.thefuckingbutton')
  hambutton.style.display = 'none'
}
function hideHamburger(){
  const sidebar = document.querySelector('.hamb')
  sidebar.style.display = 'none'
  const hambutton = document.querySelector('.thefuckingbutton')
  hambutton.style.display = 'flex'
}
function shownaturnav(){
  const hideit = document.querySelector('.hamb')
  hideit.style.display = 'none'
  const showit = document.querySelector('.hideondesk')
  showit.style.display = 'flex'

}

function checkPageWidth() {
  if (window.innerWidth > 1300) {
    shownaturnav();
  }
}
window.addEventListener('resize', checkPageWidth);

window.addEventListener('load', checkPageWidth);