#!/usr/bin/node
/* A function that returns the number of occurrences in a list. */
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      occ += 1;
    }
  }
  return (occ);
};
