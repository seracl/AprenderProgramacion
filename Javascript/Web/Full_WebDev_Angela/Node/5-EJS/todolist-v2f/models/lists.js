/*Mongoose imports*/
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

/*Local imports*/
const mongooseConnect = require(path.join(__dirname, 'util/mongoose.js')).mongooseConnect;
const db = require(path.join(__dirname, 'util/mongoose.js')).getDB;

/*Creating DB*/
//Create the document Schema
const listSchema = new Schema({
    name: {
        type: String
    },
    items: [{
        type: Schema.Types.ObjectId,
        ref: 'List'
    }]
});

listSchema.methods.addToList = function () {
    const itemToSave = [...this.items];
};

/*Creating and exporting the model*/
module.exports = mongoose.model('List', listSchema);  