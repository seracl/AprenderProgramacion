/*Express imports */
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const ObjectId = Schema.ObjectId;

/* Connection URL */
const url = 'mongodb://localhost:27017'; //Remember start mongod on hyper when working locally
const uri = "mongodb+srv://raulo85:raulo85@udemyangela-scuby.azure.mongodb.net/fruitsDB?retryWrites=true&w=majority";

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

/*Creating models  */
//Create the document Schema
const fruitSchema = new Schema({
    name: String,
    rating: Number,
    review: String
});
const personSchema = new Schema({
    name: String,
    age: Number,
    favouriteFruit: fruitSchema
});

//Creating a collection/model that has the schema structure
     //This ones are used for exporting the schema when using models
const Fruit = mongoose.model('Fruit', fruitSchema);
const Person = mongoose.model('Person', personSchema);

// //Creating a document
const fruit = new Fruit({ name: 'Pineapple', score: 9, review: 'Great fruit' });
// const person = new Person({ name: 'Manolo', age: 33, favouriteFruit: fruit });
// fruit.save();
// person.save();


// Fruit.insertMany([
//     { name: 'Apple', score: 8, review: 'Great fruit' },
//     { name: 'Orange', score: 6, review: 'Kind of sour' },
//     { name: 'Bananna', rating: 9, review: 'Great fruit' }
// ]);

// Person.insertMany([
//     { name: 'Raul', age: 33 },
//     { name: 'Amelia', age: 5 },
//     { name: 'Idril', age: 0.4 }
// ]);

Person.updateMany({ favouriteFruit: { $exists: false } }, { $set: { favouriteFruit: fruit } });



// Fruit.find()
//     .then(result => {
//         result.forEach(element => {
//             console.log(element.name);
//         })
//     })
//     .catch(err => {throw 'No item found in Fruits!!!'});
    
Person.find()
    .then(result => {
        result.forEach(element => {
            console.log(element.name, element._id);
            console.log(element);
        })
    })
    .catch(err => {throw 'No item found in Person!!!'});

module.exports.mongooseConnect = mongooseConnect;