#!/usr/bin/node
/* Script that display the status code of a GET request. */
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const di = {};
  let id = '';
  const array = JSON.parse(body.toString());
  for (let index = 0; index < array.length; index++) {
    if (array[index].userId.toString() in di) {
      id = array[index].userId.toString();
      if (array[index].completed === true) {
        di[id] += 1;
      }
    } else {
      id = array[index].userId.toString();
      di[id] = 0;
      if (array[index].completed === true) {
        di[id] += 1;
      }
    }
  }
  console.log(di);
});
