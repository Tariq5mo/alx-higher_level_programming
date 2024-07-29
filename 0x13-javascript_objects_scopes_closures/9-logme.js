#!/usr/bin/node
/* a function that prints the number of arguments already printed and the new argument value. */
let times = 0;
exports.logMe = function (item) {
  console.log(`${times}: ${item}`);
  times += 1;
};
