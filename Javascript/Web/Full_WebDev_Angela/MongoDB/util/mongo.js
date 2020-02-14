/*Express imports */
const mongodb = require('mongodb');
const MongoClient = mongodb.MongoClient;
const mongoose = require('mongoose');
const assert = require('assert');

/* Connection URL */
const url = 'mongodb://localhost:27017'; //Remember start mongod on hyper when working locally
const uri = "mongodb+srv://raulo85:raulo85@udemyangela-scuby.azure.mongodb.net/test?retryWrites=true&w=majority";

// Database connection
const dbName = 'fruitsDB';
const collection = 'fruits';

/* MongoDB connection */
const mongoConnect = () => {
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
    client.connect()
        .then(client => {
            const _db = client.db(dbName).collection(collection);
            console.log(`Successfully connected to MongoDB at host:"${client.s.options.servers[0].host}"!!!`);
            //findDocument(_db);
            getDB(_db);
        })
        .catch(err => {
            //console.log(err);
            throw 'Database connection failed!';
        });
    client.close();
    
    
};

//Insert some documents
const insertDocument = (_db) => { 
    //_db.insertMany([
    //     {
    //         name: 'Apple',
    //         score: 8,
    //         review: 'Great fruit'
    //     },
    //     {
    //         name: 'Orange',
    //         score: 6,
    //         review: 'Kind of sour'
    //     },
    //     {
    //         name: 'Bananna',
    //         score: 9,
    //         review: 'Great fruit'
    //     }
    // ]);
}

//Find all documents
const findAllDocuments = (_db) => {
    _db.find()
        .then(result => {
            console.log(result);
            return result;
        }).catch(err => {
            throw err
        });

}

//Find one document
const findDocument = (_db) => {
    _db.find({}).toArray()
        .then(result => {
            console.log(result);
            return result;
        }).catch(err => {
            throw err
        });

}

const getDB = (_db) => {
    if (_db) {
        return _db;
    }
    throw 'No database found!!!';
};


module.exports.mongoConnect = mongoConnect;
module.exports.getDb = getDB;