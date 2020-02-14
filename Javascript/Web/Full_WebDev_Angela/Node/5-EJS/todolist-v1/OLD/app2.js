const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");


const app = express();

//EJS
app.set("view engine", "ejs");

app.get("/", function (req, res) {

    //Check the day of the week
    var today = new Date();
    var currentDay = today.getDay();
    var day = "";


    if (currentDay === 6 || currentDay === 0) {
        day = "Weekend";
        res.sendFile(__dirname + "/weekend.html");
    } else {
        day = "Week";
        res.sendFile(__dirname + "/week.html");
    }

});


app.listen(3000, function () {
    console.log("Server running on port 3000");
});