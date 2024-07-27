#!/usr/bin/node
/* Searches the second biggest integer in the list of arguments. */
const arr = process.argv;
const a = [];
for (let i = 2; i < arr.length; i++) {
  a.push(+arr[i]);
}
if (a.length <= 1) {
  console.log(0);
} else {
  console.log(a.sort((a, b) => b - a)[1]);
}
