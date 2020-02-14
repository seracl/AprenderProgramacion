const path = require('path');

const express = require('express');

const shopController = require('../controllers/shop');

const router = express.Router();

// /product => GET
router
    .get('/', shopController.getIndex)
    .get('/products', shopController.getProducts)
    .get('/products/:productId', shopController.getProduct)
    .get('/cart', shopController.getCart);

// /product => POST
router
    .post('/cart', shopController.postCart)
    .post('/cart-delete-item', shopController.postCartDeleteProduct)
    .post('/create-order', shopController.postOrder)
    .get('/orders', shopController.getOrders);

module.exports = router;