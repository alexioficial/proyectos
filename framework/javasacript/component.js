exports.libs = {
    scripts: `
<script src="/lib/jquery-3.6.1.min.js"></script>
<script src="/lib/bootstrap.bundle.min.js"></script>
`,
    css: `
<link rel="stylesheet" href="/lib/bootstrap.min.css" crossorigin="anonymous">
`
};

exports.parseData = function(data) {
    const result = {};
    const pairs = data.split('&');
    for (const pair of pairs) {
        const [key, value] = pair.split('=');
        result[key] = value;
    }
    return result;
}