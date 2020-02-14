const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");


const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", function (req, res) {
    res.sendFile(__dirname + "/index.html");
    console.log(__dirname);

});

app.post("/", function (req, res) {

    //Tap into the classes
    var crypto = req.body.crypto;
    var fiat = req.body.fiat;
    var amount = req.body.amount;

    //Add the conversion to the url for request
    //var url = "https://"apiv2.bitcoinaverage.com/indices/global/ticker/" + crypto + fiat;
    var options = {
        url: "https://apiv2.bitcoinaverage.com/convert/global",
        method: "GET",
        qs: {
            from: crypto,
            to: fiat,
            amount: amount
        }
    };

    
    request(options, function (error, response, body) {
        var data = JSON.parse(body);
        var price = data.price;
        console.log("price: " + price);
        var currentDate = data.time;

        res.write("<p>The current date is: " + currentDate + "</P>");
        res.write("<h1>" + amount + " " + crypto + " equals " + price + " " + fiat + "</h1>");

        res.send();
    });

});



app.listen(3000, function () {
    console.log("Server started on port 3000!");
});