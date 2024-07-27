#!/usr/bin/node
/* prints the addition of 2 integers */
function add (a, b) {
  a = +a;
  b = +b;
  if (isNaN(a) || isNaN(b)) {
    console.log(NaN);
  } else {
    console.log(a + b);
  }
}
add(process.argv[2], process.argv[3]);
