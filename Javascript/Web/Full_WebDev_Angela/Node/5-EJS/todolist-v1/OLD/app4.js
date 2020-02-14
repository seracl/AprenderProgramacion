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
    console.log(currentDay);
    //var day = "";


    switch (currentDay) {
        case 0:
            day = "Sunday";
            break;
        case 1:
            day = "Monday";
            break;
        case 2:
            day = "Tuesday";
            break;
        case 3:
            day = "Wednesday";
            break;
        case 4:
            day = "Thursday";
            break;
        case 5:
            day = "Friday";
            break;
        case 6:
            day = "Satursday";
            break;
        default:
            console.log("Error: current day is equal to: " + currentDay);
    }

    res.render("list", {
        kindOfDay: day
    }); //can also be copied into both if and else

});


app.listen(3000, function () {
    console.log("Server running on port 3000");
});