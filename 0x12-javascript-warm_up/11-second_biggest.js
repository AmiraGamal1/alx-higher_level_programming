#!/usr/bin/node
const num = process.argv.slice(2);
if (num.length === 0 || num.length === 1) {
  console.log(0);
} else {
  num.sort();
  num.reverse();
  console.log(num[1]);
}
