const express = require('express');

const adminController = require('../controllers/admin');

const router = express.Router();

// /admin/add-product => GET
router
    .get('/add-product', adminController.getAddProduct)
    .get('/products', adminController.getProducts)
    .get('/edit-product/:productId', adminController.getEditProduct);

// /admin/add-product => POST
router
    .post('/add-product', adminController.postAddProduct)
    .post('/edit-product', adminController.postEditProduct)
    .post('/delete-product', adminController.postDeleteProduct);

module.exports = router;