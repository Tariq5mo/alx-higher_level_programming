#!/usr/bin/node
/*
Class Rectangle that defines a rectangle.
with an instance method called print() that prints the rectangle using the character X.
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      let square = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          square = square + 'X';
        }
        if (i < this.height - 1) {
          square = square + '\n';
        }
      }
      console.log(square);
    }
  }
};
