#!/usr/bin/node

/* myObject */
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/* increment */
myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
