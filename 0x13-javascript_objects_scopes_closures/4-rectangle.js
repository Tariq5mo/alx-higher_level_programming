#!/usr/bin/node
/*
Class Rectangle that defines a rectangle.
with an instance method called rotate() that exchanges the width and the height of the rectangle
wiht an instance method called double() that multiples the width and the height of the rectangle by 2
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    if (this.width > 0 && this.height > 0) {
      let square = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          square = square + c;
        }
        if (i < this.height - 1) {
          square = square + '\n';
        }
      }
      console.log(square);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
