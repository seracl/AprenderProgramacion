//jshint esversion:6
/*Express imports*/
require('dotenv').config();
const express = require("express");
const bodyParser = require("body-parser");

const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const ObjectId = Schema.ObjectId;
const encrypt = require('mongoose-encryption');//Encryption
const bcrypt = require('bcrypt');
const md5 = require('md5');//Hasning
const session = require('express-session');
const passport = require('passport');


/*PORT*/
let port = process.env.PORT || process.argv[2] || 3000;

/*Database connection*/
const url = 'mongodb://localhost:27017'; //Remember start mongod on hyper when working locally
const uri = `mongodb+srv://${process.env.DB_USER}:${process.env.DB_PASS}@${process.env.DB_URIHOST}/userDB?${process.env.DB_URIOPT}`;

/*Secutiry*/
const saltRounds = 10;
const myPlaintextPassword = 's0/\/\P4$$w0rD';
const someOtherPlaintextPassword = 'not_bacon';

/*Creating the express app*/
const router = express.Router();
const app = express();

/*View engine*/
app.set('view engine', 'ejs');
app.set('views', 'views'); /*Set views*/
app.use(express.static('public')); /*Serve static files*/
app.use(bodyParser.urlencoded({ extended: true })); /*Body Parser*/

/*Session*/
app.use(session({
    secret: 'Our little secret',
    resave: false,
    saveUninitialized: false

}));

app.use(passport.initialize());//Initialize passport
app.use(passport.session());//Use passport to set up sessions


/*Database connection*/
mongoose
    .connect(uri, {useNewUrlParser: true})
    .then(result => {
        console.log(`Successfully connected user: ${result.connections[0].user} to MongoDB at:"${result.connections[0].host}: ${result.connections[0].port}"!!!`)
    })
    .catch(err => {
        console.log(err);
        throw 'Database connection failed!';
    });


/*Creating models  */
//Create the document Schema and the collection/model that has the schema structure
const userSchema = new Schema({
    email: String,
    password:  String,
});

// Add any other plugins or middleware here. For example, middleware for hashing passwords
//userSchema.plugin(encrypt, { secret: process.env.SECRET, encryptedFields: ['password'] });
// This adds _ct and _ac fields to the schema, as well as pre 'init' and pre 'save' middleware,
// and encrypt, decrypt, sign, and authenticate instance methods

const User = mongoose.model('User', userSchema);

/*Setting different routes*/
app.route('/')
    .get((req, res, next) => {
        res.render('home');
    });

app.route('/login')
    .get((req, res, next) => {
        res.render('login');
    })
    .post((req, res, next) => {
        const username = req.body.username;
        const password = req.body.password;
        
        User.findOne({ email: username })
            .then(foundUser => {
                if (foundUser) {
                    bcrypt.compare(password, foundUser.password)
                        .then(result => {
                            if (result == true) {
                                res.render("secrets");
                            }
                        })
                        .catch(err => {
                            throw `Wrong password!!!\n ${err}`
                        });
                }
            })
            .catch(err => {
                throw `No user found in User!!!\n ${err}`
            });
    });

app.route('/register')
    .get((req, res, next) => {
        res.render('register');
    })
    .post((req, res, next) => {
        bcrypt.hash(req.body.password, saltRounds)
            .then(hashPass => {
                const newUser = new User({
                    email: req.body.username,
                    password: hashPass
                });
                newUser.save()
                    .then(result => {
                        console.log(result);
                        res.render('secrets');
                    })
                    .catch(err => {
                        console.log(err)
                    });
            });
    });


/*Server listener*/
app.listen(port, () => {
    console.log('The server is mounted on port: ' + port)
});