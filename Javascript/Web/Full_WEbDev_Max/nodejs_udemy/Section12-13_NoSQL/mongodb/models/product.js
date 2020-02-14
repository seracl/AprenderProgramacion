const ObjectId = require('mongodb').ObjectId;
const getDb = require('../util/database').getDb;

//Collection
const collection = 'products';

class Product {
    constructor(title, price, description, imageUrl, id, userId) {
        this.title = title;
        this.price = price;
        this.description = description;
        this.imageUrl = imageUrl;
        this._id = id ? new ObjectId(id) : null;
        this.userId = userId;
    }

    save() {
        //Connection call that allow to connect to db
        const db = getDb();
        let dbOp;

        if (this._id) {
            dbOp = db.collection(collection).updateOne({
                _id: this._id

            }, {
                $set: this
            }); //In $set, this = every this.argument we got...
        } else {
            dbOp = db.collection(collection).insertOne(this);
        }

        //Call collection I'm gonna work with
        return dbOp
            .then(result => {
                console.log(result.message.hashedName);
            })
            .catch(err => {
                throw 'Failed to call collection!';
            })
    }

    //Get all products
    static fetchAll() {
        const db = getDb();
        return db.collection(collection)
            .find()
            .toArray()
            .then(products => {
                //console.log(products);
                return products;
            })
            .catch(err => {
                throw 'Failed to fetchAll products!!!'
            });
    }

    //Get just one product
    static findById(prodId) {
        const db = getDb();
        return db
            .collection(collection)
            .findOne({
                _id: new ObjectId(prodId)
            })
        // .next()
        // .then(product => {
        //     return product;
        // })
        // .catch(err => {
        //     console.log(err);
        //     throw 'Failed to findById!!!';
        // });
    }

    //Delete just one product
    static deleteById(prodId) {
        const db = getDb();
        return db
            .collection(collection)
            .deleteOne({
                _id: new ObjectId(prodId)
            })
        // .next(() => {
        //     console.log('Product deletion on progress!!!');
        // })
        // .catch(err => {
        //     console.log(err);
        //     throw 'Failed to deleteById!!!';
        // });
    }
};

module.exports = Product;