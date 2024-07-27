#!/usr/bin/node
/* Searches the second biggest integer in the list of arguments. */
const arr = process.argv;
if (arr.length === 2 || arr.length === 3) {
  console.log(0);
} else {
  console.log(arr.sort().reverse()[1]);
}
