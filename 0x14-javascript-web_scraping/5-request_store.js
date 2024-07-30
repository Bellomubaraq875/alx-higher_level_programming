#!/usr/bin/node
// this scrupt gets the contents of a webpage into a file

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));