#!/usr/bin/node

const data = require('./101-data');

// Import the dictionary from the file
const originalDict = data.dict;

// Create a new dictionary to store occurrences by user ids
const occurrencesDict = {};

// Iterate over the original dictionary
for (const userId in originalDict) {
  const occurrences = originalDict[userId];

  // If the occurrences value is not already a key in the new dictionary, create an array for it
  if (!(occurrences in occurrencesDict)) {
    occurrencesDict[occurrences] = [];
  }

  // Push the current user id to the corresponding occurrences in the new dictionary
  occurrencesDict[occurrences].push(parseInt(userId));
}

// Print the new dictionary
console.log(occurrencesDict);
