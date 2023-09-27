// Escucha el evento scroll y agrega la clase "scrolled" cuando se desplaza hacia abajo
window.addEventListener("scroll", function() {
    const header = document.querySelector(".header");
    if (window.scrollY > 75) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
});
