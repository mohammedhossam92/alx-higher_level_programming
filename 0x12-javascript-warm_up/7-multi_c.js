#!/usr/bin/node
const occ = process.argv[2];
const converted = parseInt(occ);
if (isNaN(converted)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < converted; i++) {
    console.log('C is fun');
  }
}
