const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    const navLinksTest = document.querySelectorAll('.nav-links li a');


     burger.addEventListener('click',()=>{
        nav.classList.toggle('nav-active');

        navLinks.forEach((link)=>{
            if(link.style.animation){
                link.style.animation = ''
            }
        });

        burger.classList.toggle('toggle');
    });
   
}

navSlide();