const caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*()_+-={}[];':;><.,/?|";

function generarContrasena(cantidad = 25) {
    let resultado = "";
    for(let i = 0; i <= cantidad; i++) {
        resultado += caracteres.charAt(Math.floor(Math.random() * caracteres.length))
    }

    return resultado;
}

console.log(generarContrasena())