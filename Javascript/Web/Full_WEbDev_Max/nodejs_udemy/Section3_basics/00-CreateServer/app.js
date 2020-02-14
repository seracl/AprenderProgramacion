/* jshint esversion: 6 */


const http = require('http');

let port = process.env.PORT || process.argv[2] || 3000;

const server = http.createServer((req, res) => {
    let urll = req.url;
    let methodo = req.method;
    let headerso = req.headers;
    console.log(`The url is : ${urll}.\n The method is: ${methodo},\n and the headers are: ${headerso}`, req.headers);
    res.setHeader('Content-Type', 'text/html');
    res.write('<html>');
    res.write('<head><title>My first page</title></head>');
    res.write('<body><h1>Hello World!</h1></body>');
    res.write('<html>');
    res.end();
    //process.exit();
}).listen(port, () => {
    console.log(`Server running on port ${port}!`);
});