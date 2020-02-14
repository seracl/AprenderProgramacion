/*Nodejs imports*/
const path = require('path');

/*Express imports*/
const express = require("express");
const bodyParser = require("body-parser");
const pug = require('pug');

/*Local imports*/
const mongooseConnect = require('./util/mongoose').mongooseConnect;

/*PORT*/
let port = process.env.PORT || process.argv[2] || 3000;

/*Creating the express app*/
const app = express();

/*View engine*/
app.set('view engine', 'pug');
app.set('views', 'views');
//app.use(express.static("public"));
app.use(express.static(path.join(__dirname, 'public')));

/*Body Parser*/
app.use(bodyParser.urlencoded({ extended: true }));

/*Database connection*/
mongooseConnect();

/*Server listener*/
app.listen(port, () => {console.log('The server is mounted on port: ' + port)});