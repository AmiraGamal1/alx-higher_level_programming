#!/usr/bin/node
const process = require('process');
function add (a, b) {
  console.log(a + b);
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
