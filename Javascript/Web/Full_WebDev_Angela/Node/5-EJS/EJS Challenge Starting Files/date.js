//'use strict'

//module.exports.getDay = getDay;

//even shorter way
module.exports.getDate = function () {
    const today = new Date();
    const options = {
        weekday: "long",
        day: "2-digit",
        month: "short",
        year: 'numeric'
    };

    let da = today.toLocaleDateString("en-US", options);
    return da;
};

//function getDay() {
//    const hoy = new Date();
//    const options = {
//        day: "long"
//    };

//    return hoy.toLocaleDateString("en-US", options);
//}