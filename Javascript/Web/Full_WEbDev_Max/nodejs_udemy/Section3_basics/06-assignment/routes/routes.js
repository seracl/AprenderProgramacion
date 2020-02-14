/* jshint esversion: 6 */
/* jshint esversion: 9 */
/* jshint strict: false */
//'use strickt';

//JS core modules
const http = require('http');
const fs = require('fs');
const path = require('path');
//Node modules
//Local modules
const dirname = require('../util/path');
const views = require('../views/view');

let vv = `${dirname.views}views.js`;

let pb = [];


const requestHandler = (req, res) => {
    const url = req.url;
    const method = req.method;
    const headers = req.headers;
    if (url === '/' && method === 'GET') {
        fs.readFile(vv, function (err, html) {
            let nombre = "Codigo Facilito";
            res.writeHeader(200, {
                //"Content-Type": "text/html"
            });
            res.write(views.page.header);
            res.write(views.page.navBar);
            res.write(views.page.home);
            res.write(views.page.footer);
            res.end();
        });
    } else if (url === '/user' && method === 'GET') {
        fs.readFile(vv, function (err, html) {
            res.writeHeader(200, {
                //"Content-Type": "text/html"
            });
            res.write(views.page.header);
            res.write(views.page.navBar);
            res.write(views.page.user);
            res.write(views.page.footer);
            res.end();
        });
    }

    if (url === '/create-user' && method === 'POST') { 
        const body = [];
        req.on('data', (chunk) => {
            //console.log('Chunk: ', chunk, '\nChunk STR: ', chunk.toString());
            body.push(chunk);
            //console.log('Body: ', body, '\nBody STR: ', body.toString());
        });
        req.on('end', (chunk) => {
            const parsedBody = Buffer.concat(body).toString().split('=')[1];
            pb.push(parsedBody);
            
            
        });
        res.statusCode = 302;
        res.setHeader('Location', `/user`);
        //res.write(`<li>${parsedBody}</li>`);
        res.end();  
    }
};

module.exports.handler = requestHandler;
module.exports.pb = pb;

