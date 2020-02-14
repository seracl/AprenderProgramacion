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
    } else {
        day = "Week";
    }

    res.render("list", {kindOfDay: day}); //can also be copied into both if and else

});


app.listen(3000, function () {
    console.log("Server running on port 3000");
});