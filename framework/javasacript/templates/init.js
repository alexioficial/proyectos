const base = require('../templates/base.js');
const content = `
<h1>Hola</h1>asd asd f
`;
exports.code = base.BaseHTML('hola', content, ['/scripts/init.js']);