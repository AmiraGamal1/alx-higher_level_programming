#!/usr/bin/node
const num = process.argv.slice(2);
if (num.length === 0 || num.length === 1) {
  console.log(0);
} else {
  const uniqe = [...new Set(num.sort())];
  console.log(uniqe[uniqe.length - 2]);
}
