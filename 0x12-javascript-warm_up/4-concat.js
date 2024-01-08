#!/usr/bin/node

const length = process.argv.length;
const firstArg = process.argv[2];
const secondArg = process.argv[3];

if (length === 2) {
  console.log('undefined is undefined');
} else if (length === 3) {
  console.log(firstArg + ' is undefined');
} else {
  console.log(firstArg + ' is ' + secondArg);
}
