//Med cmd skapar man fil med: type null > file.extension

const express = require("express");
const bodyParser = require("body-parser");


const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
console.log(bodyParser.urlencoded({ extended: true }));

//What should happen when the browser get in touch with the server and make a get request
app.get("/", function (req, res) {
    console.log(__dirname);
    res.sendFile(__dirname + "/index.html");
});

app.post("/", function (req, res) {
    var num1 = Number(req.body.num1);
    var num2 = Number(req.body.num2);
    var result = num1 + num2;
    res.send("The result of this calculation is: " + result);
});

app.get("/bmicalculator", function (req, res) {
    res.sendFile(__dirname + "/bmiCalculator.html");
});

app.post("/bmicalculator", function (req, res) {
    var w = parseFloat(req.body.weight);
    var h = parseFloat(req.body.height);
    var bmi = parseFloat(w / (h * h));
    res.send("Your BMI is: " + bmi);
});


//Tell where to listen
app.listen(3000, function () {
    console.log("Server started at port 3000!");
});
