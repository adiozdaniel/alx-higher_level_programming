#!/usr/bin/node

/* call me */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
