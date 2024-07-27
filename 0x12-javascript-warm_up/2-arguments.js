#!/usr/bin/node
/* Prints a message depending of the number of arguments passed */
const args = process.argv;
const lenArgs = args.length;
console.log(lenArgs);
if (lenArgs <= 2) {
  console.log('No argument');
} else if (lenArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
