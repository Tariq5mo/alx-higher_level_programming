#!/usr/bin/node
/* prints the addition of 2 integers */
exports.add = function (a, b) {
  a = +a;
  b = +b;
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return (a + b);
  }
};
