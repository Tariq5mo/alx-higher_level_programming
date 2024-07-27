#!/usr/bin/node
/* Prints x times “C is fun”. */
const x = +process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let times = 0; times < x; times++) {
    console.log('C is fun');
  }
}
