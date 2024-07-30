const libs = require('../component.js').libs;
exports.BaseHTML = (title, content, scripts) => {
    var scriptsstring = '';
    scripts.forEach(script => {
        scriptsstring += `<script src="${script}"></script>\n`
    });
    return `
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ${libs.css}
    <title>${title}</title>
</head>
<body>  
    ${content}
    ${libs.scripts}
    ${scriptsstring}
</body>
</html>`;
}