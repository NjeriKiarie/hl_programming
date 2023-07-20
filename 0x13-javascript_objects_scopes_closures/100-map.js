#!/usr/bin/node
// a script that imports an array and computes a new array.
// Script must import list from the file 100-data.js
// You must use a map.
// Print both the initial list and the new list

const list = require('./100-data.js').list;
console.log(list);
const newList = list.map((x, index) => x * index);
console.log(newList);
