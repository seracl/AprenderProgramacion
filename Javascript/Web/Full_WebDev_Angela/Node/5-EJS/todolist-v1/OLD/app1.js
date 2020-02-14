const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");


const app = express();

app.get("/", function (req, res) {

    //Check the day of the week
    var today = new Date();
    if (today.getDate() === 6 || today.getDate() === 0) {
        res.send("<h1>Its weekend</h1>");
    } else {
        res.write("<h1>Its not weekend</h1>");
        res.write("<p>I have to go to work.</p>");
        res.send();
    }

});


app.listen(3000, function () {
    console.log("Server running on port 3000");
});