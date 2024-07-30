const http  = require('http');
const url   = require('url');
const fs    = require('fs');
const path  = require('path');
const tools = require('./lib/tools.js');

const templates = {
    init: require('./templates/init.js').code
};

const hostname = 'localhost';
const port = 7100;

http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);
    let ruta = parsedUrl.pathname;
    if (ruta.startsWith('/lib/')) {
        let filePath = path.join(__dirname, ruta);

        fs.readFile(filePath, (err, data) => {
            if (err) {
                console.error(`Error al leer el archivo ${filePath}:`, err);
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('404 Not Found');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/javascript' });
                res.end(data);
            }
        });
    } else {
        tools.Route(ruta, '/', req, res, templates.init, ['GET', () => {}]);
    }
}).on('error', (err) => {
    console.error('Error en el servidor:', err);
}).listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}`);
});