#!/usr/bin/node
/* Computes and prints a factorial */
function fac (num) {
  if (num >= 1) { return num * fac(num - 1); } else { return (1); }
}
console.log(fac(+process.argv[2]));
