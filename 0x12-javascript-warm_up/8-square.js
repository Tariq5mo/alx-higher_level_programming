#!/usr/bin/node
/* Prints a square. */
const size = +process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  let square = '';
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      square = square + 'X';
    }
    if (i < size - 1) {
      square = square + '\n';
    }
  }
  console.log(square);
}
