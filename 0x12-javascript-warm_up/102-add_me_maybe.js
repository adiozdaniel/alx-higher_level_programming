#!/usr/bin/node

/** addMe */
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
