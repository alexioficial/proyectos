const listas = document.querySelectorAll('li');
listas.forEach(i => {
    i.addEventListener('click', () => {
        location.href = `lenguajes/${i.classList}`
    });
});