const mysql = require('mysql2');
const Sequelize = require('sequelize/index');

const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    database: 'node-complete',
    password: 'JRDCmysql'
});

module.exports = pool.promise();



const sequelize = new Sequelize('node-complete', 'root', 'JRDCmysql', {
  dialect: 'mysql',
  host: 'localhost'
});
module.exports = sequelize;