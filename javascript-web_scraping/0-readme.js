#!/usr/bin/node

// readFile.js

const fs = require('fs');

// Get the file path from command-line arguments
const filePath = process.argv[2];

if (!filePath) {
  console.log('Usage: node readFile.js <file_path>');
  process.exit(1);
}

// Read the file in utf-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

