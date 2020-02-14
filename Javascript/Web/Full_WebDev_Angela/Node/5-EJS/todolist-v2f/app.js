//jshint esversion:6
/*Nodejs imports*/
const path = require('path');

/*Express imports*/
const express = require("express");
const bodyParser = require("body-parser");

/*Local imports*/
const mongooseConnect = require(path.join(__dirname, 'util/mongoose.js')).mongooseConnect;


/*PORT*/
let port = process.env.PORT || process.argv[2] || 3000;

/*Creating the express app*/
const app = express();

/*View engine*/
app.set('view engine', 'ejs');
const itemsRoute = require(path.join(__dirname, 'routes/items.js'));

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, 'public')));

/*Setting different routes*/
app.use(itemsRoute);

/*Database connection*/
mongooseConnect();

/*Server listener*/
app.listen(port, () => {console.log('The server is mounted on port: ' + port)});
