exports.Route = (rutador, routename, req, res, template, method) => {
    if (rutador === routename && req.method === method[0]) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(String(template));
        method[1]();
        console.log(`${method[0]} ${rutador} [200]`);
    } else {
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.end('404 Not Found');
        console.log(`404 Not Found: ${req.method} ${rutador}`);
    }
}