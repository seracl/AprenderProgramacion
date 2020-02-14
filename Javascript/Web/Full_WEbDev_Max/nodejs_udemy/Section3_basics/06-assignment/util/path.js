/* jshint esversion: 6 */
/* jslint node: true */
/* jshint strict: false */
// 'use strict';
const path = require('path');

module.exports = {
    rootApp: process.mainModule.filename,
    root: path.dirname(process.mainModule.filename),
    public: path.dirname(process.mainModule.filename).concat('\\public\\'),
    routes: path.dirname(process.mainModule.filename).concat('\\routes\\'),
    views: path.dirname(process.mainModule.filename).concat('\\views\\'),
    
    __workFolder: function (path, split, place) {
        let rootReverseString =  path.toString().split(split);
        let rootSelect = rootReverseString.reverse()[place];
        return{
            rootReverseString: rootReverseString,
            rootSelect: rootSelect
        };
    },    
};

