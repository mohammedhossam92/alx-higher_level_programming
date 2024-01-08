#!/usr/bin/node

// get the arg and convert it to int
const firstArg = process.argv[2];
const firstArgInt = parseInt(firstArg);

function factorial (n) {
  if (!n) {
    return 1;
  } else {
    if (n === 1) {
      return n;
    } else {
      return n * factorial(n - 1);
    }
  }
}

const fact = factorial(firstArgInt);
console.log(fact);
