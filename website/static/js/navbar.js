let menu = document.querySelector('.hamburger');
menu.onclick = function(){
    navBar = document.querySelector(".navbar");
    textToHide = document.querySelector(".to-hide-from-navbar")
    navBar.classList.toggle("active");
    textToHide.classList.toggle("toHide");    
}


window.addEventListener('scroll', stickHeader);

function stickHeader(){
    var header = document.querySelector("header");
    header.classList.toggle('sticky', window.scrollY > 0);
}