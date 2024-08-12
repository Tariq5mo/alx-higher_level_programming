#!/usr/bin/node
/* Script that display the status code of a GET request. */
const request = require("request");

request.get(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      ti = JSON.parse(body.toString());
      console.log(ti["title"]);
    }
  }
);
