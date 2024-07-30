var musica = document.getElementById('music-directory');
var songs_elem = document.getElementById('songs');
var audioPlayer = document.getElementById('audioPlayer');

function esAudio(str) {
    const regex = /\.(mp3|wav|aac|flac|ogg|m4a|aiff)$/i;
    return regex.test(str);
}

musica.addEventListener('change', async e => {
    var archivos = e.target.files;
    var html = '';
    var contador = 0;
    var i = 0;
    while (i < archivos.length) {
        var nombrearchivo = archivos[i].name;
        if (esAudio(nombrearchivo)) {
            contador += 1;
            html += `
                <li class="song" song_num="${contador}">${nombrearchivo}</li>
            `;
        }
        i++;
    }
    songs_elem.innerHTML = html;

    var canciones = document.querySelectorAll('.song');
    canciones.forEach(element => {
        element.addEventListener('click', async e => {
            var songNum = e.target.getAttribute('song_num');
            var audioFilePath = archivos[songNum - 1]; // -1 porque el índice es 0-based
            var objectURL = URL.createObjectURL(audioFilePath);
            audioPlayer.src = objectURL;
            audioPlayer.play();

            // Obtener miniatura
            const metadata = await musicMetadata.parseBlob(audioFilePath);
            if (metadata.common && metadata.common.picture && metadata.common.picture.length > 0) {
                const picture = metadata.common.picture[0];
                const blob = new Blob([picture.data], { type: picture.format });
                const imageUrl = URL.createObjectURL(blob);
                console.log('Miniatura encontrada:', imageUrl);
            } else {
                console.log('No se encontró una miniatura incrustada en los metadatos.');
            }
        });
    });
});
