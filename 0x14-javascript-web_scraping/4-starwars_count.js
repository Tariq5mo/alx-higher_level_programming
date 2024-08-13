#!/usr/bin/node
/* Script that display the status code of a GET request. */
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  } else {
    let i = 0;
    const ti = JSON.parse(body.toString());
    for (let index = 0; index < ti.results.length; index++) {
      for (
        let ind = 0;
        ind < ti.results[index].characters.length;
        ind++
      ) {
        if (
          ti.results[index].characters[ind] ===
          'https://swapi-api.alx-tools.com/api/people/18/'
        ) {
          i += 1;
        }
      }
    }
    console.log(i);
  }
});
