//TODO Requireing modules
const path = require("path"); //JS modules
const express = require("express"); //Node core modules
const bodyParser = require("body-parser");
const pug        = require("pug");


//TODO Global variables
const port = process.env.PORT || process.argv[2] || 3000;
//const hostname = "127.0.0.1";

//TODO Mounting the app and engines
const app = express();
app.set('view engine', 'ejs');
app.set('views', 'views');

//TODO Necesary complements
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname, 'public')));

console.log(process);

//TODO Server
app.listen(port, hostname, () => {
    //console.log(`Server running at http://${hostname}:${port}/`);
    console.log(`Worker ${process.pid} started`);
});