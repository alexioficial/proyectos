function binary_encode(s){
    s = unescape(encodeURIComponent(s));
    var chr, i = 0, l = s.length, out = '';
    for( ; i < l; i ++ ){
        chr = s.charCodeAt(i).toString(2);
        while( chr.length % 8 != 0 ){ chr = '0' + chr; }
        out += chr;
    }
    return out;
}

function binary_decode(s){
    var i = 0, l = s.length, chr, out = '';
    for( ; i < l; i += 8 ){
        chr = parseInt(s.substr(i, 8), 2).toString(16);
        out += '%' + ((chr.length % 2 == 0) ? chr : '0' + chr);
    }
    return decodeURIComponent(out);
}

const texto = document.getElementById('texto');
const btnBin = document.getElementById('btnBin');
const btnTxt = document.getElementById('btnTxt');
const contenido = document.getElementById('contenido');

btnBin.addEventListener('click', () => {
    contenido.value = binary_encode(texto.value);
});

btnTxt.addEventListener('click', () => {
    contenido.value = binary_decode(texto.value);
});