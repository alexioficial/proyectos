const tools = {
    PostBack: (datos, ruta, callback) => {
        $.ajax({
            type: "POST",
            url: ruta,
            data: JSON.stringify(datos),
            contentType: "application/json",
            success: function (response) {
                callback(response);
            }
        });
    },
    Enter: (idcontrol, callback) => {
        var control = document.getElementById(idcontrol);
        control.addEventListener('keydown', e => {
            if (e.key == 'Enter') {
                callback();
            }
        });
    }
};