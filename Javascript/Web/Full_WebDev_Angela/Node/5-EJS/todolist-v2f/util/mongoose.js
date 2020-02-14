/*Mongoose imports */
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
//const ObjectId = Schema.ObjectId;

/* Connection URL */
//const url = 'mongodb://localhost:27017'; //Remember start mongod on hyper when working locally
const uri = "mongodb+srv://raulo85:raulo85@udemyangela-scuby.azure.mongodb.net/todoListsDB?retryWrites=true&w=majority";

/*Database connection*/
const mongooseConnect = () => {
    mongoose
    .connect(uri, {useNewUrlParser: true})
        .then(result => {  
        console.log(`Successfully connected to MongoDB at host:"${result.connections[0].host}"!!!`); 
    
    })
    .catch(err => {
        console.log(err);
        throw 'Database connection failed!';
    });
};

/*Accessing databaseModel*/
const getDB = () => {
    if (_db) {
        return _db;
    }
    throw 'No database found!!!';
};

/*Exporting the module*/
module.exports.mongooseConnect = mongooseConnect;
module.exports.getDb = getDB;