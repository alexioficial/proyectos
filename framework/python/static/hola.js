function PostBack(ruta, datos, callback) {
    $.ajax({
        type: "POST",
        url: ruta,
        data: JSON.stringify(datos),
        contentType: "application/json",
        success: function (response) {
            callback(response);
        }
    });
}

PostBack('/test/hola', {'hola': 'adios'}, data => {
    console.log(data);
})