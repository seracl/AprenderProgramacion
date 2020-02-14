// const ObjectId = require('mongodb').ObjectId;
// const getDb = require('../util/database').getDb;

// //Collection
// const collection = 'users';

// class User {
//     constructor(username, email, cart, id) {
//         this.name = username;
//         this.email = email;
//         this.cart = cart; //{items: []}
//         this._id = id ? new ObjectId(id) : null;
//     }

//     save() {
//         const db = getDb();
//         return db.collection(collection).insertOne(this);
//     }
//     // save() {
//     //     //Connection call that allow to connect to db
//     //     const db = getDb();
//     //     let dbOp;

//     //     if (this._id) {
//     //         dbOp = db.collection(collection).updateOne({
//     //             _id: this._id

//     //         }, {
//     //             $set: this
//     //         }); //In $set, this = every this.argument we got...
//     //     } else {
//     //         dbOp = db.collection(collection).insertOne(this);
//     //     }

//     //     //Call collection I'm gonna work with
//     //     return dbOp
//     //         .then(result => {
//     //             console.log(result.message.hashedName);
//     //         })
//     //         .catch(err => {
//     //             throw 'Failed to call collection!';
//     //         })
//     // }

//     addToCart(product) {
//         // const cartProduct = this.cart.items.findIndex(cp => {
//         //     return cp._id === product._id;
//         // });
//         const updatedCart = {
//             items: [{
//                 productId: new ObjectId(product._id),
//                 quantity: 1
//             }]
//         };
//         const db = getDb();
//         db.collection(collection).updateOne({
//             _id: new ObjectId(this._id)
//         }, {
//             $set: {
//                 cart: updatedCart
//             }
//         });

//     }

//     // //Get all products
//     // static fetchAll() {
//     //     const db = getDb();
//     //     return db.collection(collection)
//     //         .find()
//     //         .toArray()
//     //     // .then(products => {
//     //     //     //console.log(products);
//     //     //     return users;
//     //     // })
//     //     // .catch(err => {
//     //     //     throw 'Failed to fetchAll products!!!'
//     //     // });
//     // }

//     //Get just one user
//     static findById(userId) {
//         const db = getDb();
//         return db
//             .collection(collection)
//             .findOne({
//                 _id: new ObjectId(userId)
//             })
//             .then(user => {
//                 return user;
//             })
//             .catch(err => {
//                 console.log(err);
//                 throw 'Failed to findById!!!';
//             });
//     }

//     // //Delete just one product
//     // static deleteById(userId) {
//     //     const db = getDb();
//     //     return db
//     //         .collection(collection)
//     //         .deleteOne({
//     //             _id: new ObjectId(userId)
//     //         })
//     //     // .next(() => {
//     //     //     console.log('Product deletion on progress!!!');
//     //     // })
//     //     // .next()
//     //     // .catch(err => {
//     //     //     console.log(err);
//     //     //     throw 'Failed to deleteById!!!';
//     //     // });
//     // }
// };

// module.exports = User;