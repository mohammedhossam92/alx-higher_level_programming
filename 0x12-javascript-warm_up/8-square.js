#!/usr/bin/node
const occ = process.argv[2];
const converted = parseInt(occ);
if (isNaN(converted)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < converted; i++) {
    let row = ''
    for (let x = 0; x < converted; x++) {
	  row += 'x';
     }
    console.log(row);
  }
}
