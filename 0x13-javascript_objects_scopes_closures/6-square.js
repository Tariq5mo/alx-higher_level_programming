#!/usr/bin/node
/* Square class that defines a square and inherits from Rectangle of 4-rectangle.js */
const Square = require('./5-square');

module.exports = class good extends Square {
  charPrint (c) {
    super.print(c);
  }
};
