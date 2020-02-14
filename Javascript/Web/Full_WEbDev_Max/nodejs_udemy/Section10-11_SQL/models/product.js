const Sequelize = require('sequelize/index');

const sequelize = require('../util/database');

const Product = sequelize.define('product', {
  id: {
    type: Sequelize.INTEGER,
    autoIncrement: true,
    allowNull: false,
    primaryKey: true,
    validate: {
      notEmpty: true,
      len: [2,10]
    }
  },
  title: Sequelize.TEXT,
  price: {
    type: Sequelize.DECIMAL(10, 2),
    allowNull: false
  },
  imageUrl: {
    type: Sequelize.STRING,
    allowNull: false, 
    validate: {
      isUrl: {
        msg: 'SSO URL must be a valid url.'
      },
      notNull: {
        msg: 'Done!!!',
      }
    }
  },
  description: {
    type: Sequelize.STRING,
    allowNull: false
  }
});

module.exports = Product;