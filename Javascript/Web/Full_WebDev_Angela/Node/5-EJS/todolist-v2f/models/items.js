/*Nodejs imports*/
const path = require('path');

/*Mongoose imports*/
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

/*Local imports*/
const mongooseConnect = require(path.join(__dirname, 'util/mongoose.js')).mongooseConnect;
const db = require(path.join(__dirname, 'util/mongoose.js')).getDB;

/*Creating DB*/
//Create the document Schema
const itemSchema = new Schema({
    name: {
        type: String,
        require: true
    }
});

/*Creating and exporting the model*/
module.exports = mongoose.model('Item', itemSchema);