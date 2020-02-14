const express = require("express");

const app = express();

//What should happen when the browser get in touch with the server and make a get request
app.get("/", function (req, res) {
    res.send("<h1>Hello, World</h1>");
});

app.get("/contact", function (req, res) {   
    res.send("Contact me at Raul gmail");
});

app.get("/about", function (req, res) {
    res.send("My name is Raul and I love manga");
});

app.get("/hobbies", function (req, res) {
    res.send("Cinema, sport, dancing");
});

//Tell where to listen
app.listen(3000, function () {
    console.log("Server started at port 3000!");
});

//C:\\Development\\WD\\Javascript\\Dicee Challenge - Starting Files\\