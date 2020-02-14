
//'use strict'

//Everything I want exported has to get its own module.export
//module.exports = getDate; bounds the whole module to that function 
//while the subsecuents allow as said to export multiple functions
module.exports.getDay = getDay;

//even shorter way
module.exports.getDate = function () {
    const today = new Date();
    const options = {
        //localMatcher: "lookup",
        //timeZone: "Europe/Stockholm",
        //hour12: "false",
        //hourCycle: "h24",
        //formatMatcher: "best fit",
        //era: "long",
        weekday: "long",
        day: "2-digit",
        month: "short",
        year: 'numeric'
        //day: "numeric",
        //hour: "numeric",
        //minute: "numeric"
        //second: "numeric"
        //timeZoneName: "short"

    };

    let day = today.toLocaleDateString("en-US-u-hc-swedish", options);
    //let day = today.toLocaleDateString("sv-SE-u-hc-swedish", options);
    return day;
}

function getDay() {
    const today = new Date();
    const options = {
        day: "short"
    };

    return today.toLocaleDateString("en-US-u-hc-swedish", options);
}