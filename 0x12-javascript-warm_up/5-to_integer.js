#!/usr/bin/node
const process = require('process');
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log(parseInt(process.argv[2]));
}
