#!/usr/bin/node
/* Script that gets the contents of a webpage and stores it in a file. */
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const content = body.toString();

  fs.writeFile(process.argv[3], content, 'utf-8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
