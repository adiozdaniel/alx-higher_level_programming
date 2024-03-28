#!/usr/bin/node

/* logme */
let count = 0;
exports.logMe = function (item) { console.log(`${count++}: ${item}`); };
