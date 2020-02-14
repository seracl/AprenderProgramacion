const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");
const fullICU = require('full-icu');

//Module locally created
const date = require("./date.js");
let d = date.getDate();  //"OLD/app5.js" shows a different way, but in this one I call the function directly
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

    res.render("list", { listTitle: d, newListItems: items });
    //I can also create a variable here inside the get, or just call it from d as Ive done here

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


app.listen(3500, function () {
    console.log("Server running on port 3500");
});