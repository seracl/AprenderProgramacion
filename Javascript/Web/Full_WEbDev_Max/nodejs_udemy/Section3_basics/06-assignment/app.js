/* jshint esversion: 6 */
/* jslint node: true */
/* jshint strict: true */
'use strict';

//JS core modules
const http = require('http');

//Node modules
//Local modules
const routes = require('./routes/routes');
const dirname = require('./util/path');
// console.log('root: ', dirname.root);
// console.log('rs: ', `/${dirname.__workFolder(dirname.routes, '\\', 1).rootSelect}`);

const port = process.env.PORT || process.argv[2] || 3000;
const hostname = process.env.Test;

// console.log('dirname app: ', routes._dirname);


const server = http.createServer(routes.handler).listen(port, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});