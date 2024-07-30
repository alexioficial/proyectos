$('#tablacontenedora').html($('#htmltable').val());

function ParseTable() {
    var tabla = document.getElementById('tablacontenedora');
    var datos = [];
    
    for (var i = 0; i < tabla.rows.length; i++) {
        var fila = tabla.rows[i];
        var filaDatos = [];
    
        for (var j = 0; j < fila.cells.length; j++) {
            var celda = fila.cells[j];
            var input = celda.querySelector('input');
            if (input.value === '') {
                input.value = 0;
            }
            filaDatos.push(parseInt(input.value, 10));
        }
        datos.push(filaDatos);
    }
    
    return datos;
}

function Solve() {
    tools.PostBack({d: ParseTable()}, '/Solve', data => {
        if (data.estatus == 0) {
            var tabla = document.getElementById('tablacontenedora');
            for (var i = 0; i < tabla.rows.length; i++) {
                var fila = tabla.rows[i];
                for (var j = 0; j < fila.cells.length; j++) {
                    var celda = fila.cells[j];
                    var input = celda.querySelector('input');
                    input.value = data.res[i][j].toString();
                }
            }
        } else {
            alert(data.msj);
        }
    });
}

function Clear() {
    var tabla = document.getElementById('tablacontenedora');
    for (var i = 0; i < tabla.rows.length; i++) {
        var fila = tabla.rows[i];
        for (var j = 0; j < fila.cells.length; j++) {
            var celda = fila.cells[j];
            var input = celda.querySelector('input');
            input.value = ''; // Limpiar el valor del input
        }
    }
}

document.getElementById('solve').addEventListener('click', () => {
    Solve();
});

document.getElementById('clear').addEventListener('click', () => {
    Clear();
});

document.addEventListener("keydown", e => {
    var elem = e.target.id;
    var elemsplit = elem.split('_');
    var n1 = elemsplit[1];
    var n2 = elemsplit[2];
    if(e.key === "ArrowUp") {
        $(`#i_${~~n1 - 1}_${n2}`).focus();
    } else if(e.key === "ArrowDown") {
        $(`#i_${~~n1 + 1}_${n2}`).focus();
    } else if(e.key === "ArrowLeft") {
        $(`#i_${n1}_${~~n2 - 1}`).focus();
    } else if(e.key === "ArrowRight") {
        $(`#i_${n1}_${~~n2 + 1}`).focus();
    }
});