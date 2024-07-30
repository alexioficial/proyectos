const codigo = document.getElementById('codigo');
const nombre = document.getElementById('nombre');
const evento = document.getElementById('evento');
document.addEventListener('keydown', function(e) {
    codigo.innerText = e.keyCode;
    nombre.innerText = e.key;
    evento.innerText = e.code;
});