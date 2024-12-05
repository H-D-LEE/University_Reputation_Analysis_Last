const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const fs = require('fs');

const dbDir = path.resolve(__dirname, 'data');
const dbPath = path.join(dbDir, 'database.db');

console.log(`Database directory: ${dbDir}`);
