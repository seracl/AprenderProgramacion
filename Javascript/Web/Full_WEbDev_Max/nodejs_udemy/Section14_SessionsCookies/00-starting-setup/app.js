const path = require('path');

const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

let port = process.env.PORT || process.argv[2] || 3000;

const errorController = require('./controllers/error');
const User = require('./models/user');

const app = express();

app.set('view engine', 'ejs');
app.set('views', 'views');

const adminRoutes = require('./routes/admin');
const shopRoutes = require('./routes/shop');
const authRoutes = require('./routes/auth');

app.use(bodyParser.urlencoded({
    extended: false
}));
app.use(express.static(path.join(__dirname, 'public')));

app.use((req, res, next) => {
    User.findById('5d5a80a724fc173f0de598c4')
        .then(user => {
            req.user = user;
            next();
        })
        .catch(err => console.log(err));
});

app.use('/admin', adminRoutes);
app.use(shopRoutes);
app.use(authRoutes);

app.use(errorController.get404);

// Connection URL
const url = 'mongodb://localhost:27017'; //Remember start mongod on hyper when working locally
const uriMax = "mongodb+srv://raulo85:raulo85@udemymax-i5ibg.azure.mongodb.net/shop?retryWrites=true&w=majority";

// Database connection
mongoose
    .connect(uriMax, {
        useNewUrlParser: true
    })
    .then(result => {
        User.findOne()
            .then(user => {
                if (!user) {
                    const user = new User({
                        name: 'Raul',
                        email: 'raul@casa.se',
                        cart: {
                            items: []
                        }
                    });
                    user.save();
                }
            })
            .catch(err => {
                throw 'Already existing user!'
            });
        console.log(`Successfully connected to MongoDB at host:"${result.connections[0].host}"!!!`);
    })
    .catch(err => {
        //console.log(err);
        throw 'Database connection failed!';
    });

app.listen(port, () => {
    console.log('The server is mounted on port: ' + port);
});