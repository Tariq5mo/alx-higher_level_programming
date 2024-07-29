#!/usr/bin/node
/*  a function that returns the reversed version of a list. */
exports.esrever = function (list) {
  let second = list.length - 1;
  let temp = 0;
  for (let fisrt = 0; fisrt < second; fisrt++, second--) {
    temp = list[fisrt];
    list[fisrt] = list[second];
    list[second] = temp;
  }
  return (list);
};
