const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");

const app = express();
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", function (req, res) {
    res.sendFile(__dirname + "/signup.html");
    console.log(__dirname);
});


app.post("/", function (req, res) {
    var firstName = req.body.firstName;
    var lastName = req.body.lastName;
    var email = req.body.email;
    console.log(firstName, lastName, email);

    var data = {
        members: [
            {
                email_address: email,
                status: "subscribed",
                merge_fields: {
                    FNAME: firstName,
                    LNAME: lastName
                }

            }
        ]
    };

    var jsonData = JSON.stringify(data);

    var options = {
        url: "https://us20.api.mailchimp.com/3.0/lists/689dba982e",
        method: "POST",
        headers: {
            "Authorization": "Raul d64860c692ac9e52a2353964e6c03666-us20"
        },
        body: jsonData
    };

    request(options, function (error, response, body) {
        if (error) {
            res.sendFile(__dirname + "/failure.html");
            //res.send("There was an error with signing up, please try again!");
            console.log(error);
        } else {
            if (response.statusCode === 200) {
                res.sendFile(__dirname + "/success.html");
            } else {
                res.sendFile(__dirname + "/failure.html");
            }
        }
    });

});

app.post("/failure", function (req, res) {
    res.redirect("/");
});

app.listen(3000, function () {
    console.log("Server running on port 3000.");
});


//API key: d64860c692ac9e52a2353964e6c03666-us20
//ListID: 689dba982e