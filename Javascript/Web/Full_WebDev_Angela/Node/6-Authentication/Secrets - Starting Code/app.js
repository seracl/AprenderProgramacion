//jshint esversion:6
/*Express imports*/
require('dotenv').config();
const express = require("express");
const bodyParser = require("body-parser");

const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const ObjectId = Schema.ObjectId;
const session = require('express-session');
const passport = require('passport');
const passportLM = require('passport-local-mongoose');



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
    secret: 'Our little secret.',
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

mongoose.set('useCreateIndex', true);

/*Creating models  */
//Create the document Schema and the collection/model that has the schema structure
const userSchema = new Schema({
    email: String,
    password:  String,
});

userSchema.plugin(passportLM);

const User = mongoose.model('User', userSchema);

passport.use(User.createStrategy());
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

/*Setting different routes*/
app.route('/')
    .get((req, res, next) => {
        res.render('home');
	});
	
app.get('/secrets', function (req, res) {
		if (req.isAuthenticated()) {
			res.render('secrets');
		} else {
			res.redirect('/login');
		}
	});

app.route('/login')
    .get((req, res, next) => {
        res.render('login');
    })
    .post((req, res, next) => {
        //
    });
	

app.route('/register')
    .get((req, res, next) => {
        res.render('register');
    })
    .post((req, res, next) => {
		User.register({ username: req.body.username }, { password: req.body.password }, function (err, user) {
			if (err) {
				res.redirect('/register');
				throw err;
			} else {
				passport.authenticate('local')(req, res, function () {
					res.redirect('/secrets');
				})
			}
		});
    });


/*Server listener*/
app.listen(port, () => {
    console.log('The server is mounted on port: ' + port)
});