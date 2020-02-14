/*Nodejs imports*/
//require('dotenv').config();
const path = require('path');

/*Express imports*/
const express = require("express");
const bodyParser = require("body-parser");
const pug = require("pug");
var results = require('norsk-tipping');

/*Global Variables*/
let port = process.env.PORT || process.argv[2];
const hostname = "127.0.0.1";

/*Creating the express app*/
const app = express();
app.set('view engine', 'ejs');
app.set('views', 'views');

/*Body Parser*/
app.use(bodyParser.urlencoded({extended: true})); //app.use(bodyParser.urlencoded({ extended: true })); //x-www-form-urlencoded <form>
app.use(express.static(path.join(__dirname, 'public'))); //app.use(bodyParser.json()); //application/json

/*Manage routes*/

/*TEST*/
var options = {
	type: 'vikinglotto',
	range: {
			fromDrawID: 1050,
			toDrawID: 1051
	}
};


results(options)
	.then(function (response) {
			console.log(response);
	}).catch(function (err) {
			console.log(err);
	});

/*Server listener*/
app.listen(port, hostname, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
	console.log(`Worker ${process.pid} started`);
});