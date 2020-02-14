// JavaScript source code
const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");
const fullICU = require('full-icu');

//Module locally created
const date = require("./date.js");
let d = date.getDate;
console.log(date);

const app = express();

//EJS
app.set("view engine", "ejs");

let items = ["Buy Food", "Cook Food", "Eat Food"];
let workItems = [];

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));


//Targetting the home router
app.get("/", function (_req, res) {

    let date = d();

    res.render("list", { listTitle: date, newListItems: items });

});

//Targetting the work router
app.get("/work", function (req, res) {
    res.render("list", { listTitle: "Work List", newListItems: workItems });
});

//Targetting the work router
app.get("/about", function (req, res) {
    res.render("about");
});


app.post("/", function (req, res) {
    let itemNew = req.body.newItem;

    if (req.body.list === "Work") {
        workItems.push(itemNew);
        res.redirect("/work");
        //console.log("Work items: ", workItems);
        console.log("/work: ", req.body);
    } else {
        items.push(itemNew);
        res.redirect("/"); //This line riderects me to the get request
        //console.log("Items: ", workItems);
        console.log("/: ", req.body);
    }
});










//app.post("/delete", function (req, res) {
//    let itemNew = req.body.newItem;
//    items.slice(itemNew, 1);
//    console.log(items);
//    res.redirect("/");
//});


app.listen(3000, function () {
    console.log("Server running on port 3000");
});