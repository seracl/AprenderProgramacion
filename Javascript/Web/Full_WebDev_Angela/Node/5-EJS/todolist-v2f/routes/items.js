/*Nodejs imports*/
const path = require('path');

/*Express imports*/
const express = require('express');
const router = express.Router();

/*Local imports*/
const itemController = require('../controllers/items.js');

// /route => GET
router
    .get("/", itemController.getIndex)//Render the root view
    .get("/work", itemController.getWorkItems)//Render the root view
    .get("/about", itemController.getAbout)//Render the root view

// /route => POST
router
    .post("/", itemController.postItem);

/*Exporting the module*/   
module.exports = router;