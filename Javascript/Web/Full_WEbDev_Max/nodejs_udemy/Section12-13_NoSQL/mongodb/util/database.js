const mongodb = require('mongodb');
const MongoClient = mongodb.MongoClient;

// Connection URL
const url = 'mongodb://localhost:27017'; //Remember start mongod on hyper when working locally
const uriMax = "mongodb+srv://raulo85:raulo85@udemymax-i5ibg.azure.mongodb.net:27017/test?retryWrites=true&w=majority";
const uriAngela = "mongodb+srv://raulo85:raulo85@udemyangela-scuby.azure.mongodb.net:27017/test?retryWrites=true&w=majority";
// Database connection
let _db;
const dbName = 'shop';

const mongoConnect = () => {
    const client = new MongoClient(url, {
        useNewUrlParser: true
    });
    client.connect()
        .then(client => {
            console.log(`Successfully connected to MongoDB at host:"${client.s.options.servers[0].host}"!!!`);
            _db = client.db(dbName);
            getDB();
        })
        .catch(err => {
            console.log(err);
            throw 'Database connection failed!';
        });
    client.close();
};

const getDB = () => {
    if (_db) {
        return _db;
    }
    throw 'No database found!!!';
};

module.exports.mongoConnect = mongoConnect;
module.exports.getDb = getDB;