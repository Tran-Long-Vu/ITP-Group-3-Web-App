// Import necessary modules and libraries
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const path = require('path');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');

// CORS middleware
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "http://localhost:8080");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

// Middleware for parsing the request body
app.use(bodyParser.json());

// Serve the Vue.js app as a static file
app.use(express.static(path.join(__dirname, 'dist')));

// Connect to the database
const db = new sqlite3.Database('./db/mydb.db', (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the SQLite database.');
});

// Login route
app.post('/login', (req, res) => {
  const { email, password } = req.body;

  // Query the database to check if the email and password match
  db.get('SELECT * FROM USERS WHERE email = ? AND password = ?', [email, password], (err, row) => {
    if (err) {
      console.log(err);
      res.status(500).json({ message: 'Internal server error' });
    }
    if (row) { 
      console.log(row);
      // Successful login
      res.status(200).json({ message: 'Login successful', userData: row });
    } else {
      // Invalid email or password
      res.status(401).json({ message: 'Invalid email or password' });
    }
  });
});

app.post('/calendar', (req, res) => {
  const { email, password } = req.body;

  // Query the database to check if the email and password match
  db.get('SELECT * FROM USERS WHERE email = ? AND password = ?', [email, password], (err, row) => {
    if (err) {
      console.log(err);
      res.status(500).json({ message: 'Internal server error' });
    }
    if (row) { 
      console.log(row);
      // Successful login
      res.status(200).json({ message: 'Login successful', userData: row });
    } else {
      // Invalid email or password
      res.status(401).json({ message: 'Invalid email or password' });
    }
  });
});

// Redirect all other routes to the Vue.js app
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

// Start the server
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});