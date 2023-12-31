// Import necessary modules and libraries
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const path = require('path');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');

// CORS middleware
app.use(function (req, res, next) {
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

// Model route 
app.post('/model', (req, res) => {
  const { name, timestamp } = req.body;
  if(req.body){
    console.log(req.body);
    console.log('Received data:');
    console.log('Name:', name);
    console.log('Timestamp:', timestamp);
  }
  

  // Perform any necessary database operations or data processing here
  // Query the database to check if the email and password match
  db.get(
    'SELECT UID FROM USERS WHERE name = ?',
    [name],
    (err, row) => {
      if (err) {
        console.error(err.message);
      } else if (row) {
        const uid = row.UID;
  
        // Check if the attendance record already exists for the same UID and timestamp
        db.get(
          'SELECT * FROM ATTENDANCE WHERE UID = ? AND Timestamp = ?',
          [uid, timestamp],
          (err, row) => {
            if (err) {
              console.error(err.message);
            } else if (row) {
              // Attendance record already exists, update the Status to 1
              db.run(
                'UPDATE ATTENDANCE SET Status = ? WHERE UID = ? AND Timestamp = ?',
                [1, uid, timestamp],
                function (err) {
                  if (err) {
                    console.error(err.message);
                  } else {
                    console.log('Attendance updated successfully!');
                  }
                }
              );
            } else {
              // Attendance record doesn't exist, insert a new record
              db.run(
                'INSERT INTO ATTENDANCE (UID, Timestamp, Status) VALUES (?, ?, ?)',
                [uid, timestamp, 1],
                function (err) {
                  if (err) {
                    console.error(err.message);
                  } else {
                    console.log('Attendance recorded successfully!');
                  }
                }
              );
            }
          }
        );
      } else {
        console.log('User not found.');
      }
    }
  );
  // Send a response back to the Python code
  res.status(200).send('Data received successfully from Node!');
});


// Calendar route
app.get('/calendars/:data', (req, res) => {
  if (req.params.data == "users") {
    db.all('SELECT UID, name, attendance_count, absence_count FROM USERS', (err, data) => {
      if (err) {
        console.log(err)
        res.status(500).json({ message: 'Internal server error' })
      }
      if (data) {
        res.send({ data })
      } else {
        res.status(204).json({ message: 'No user in database' })
      }
    })
  } else if (req.params.data == "attendance") {
    db.all('SELECT * FROM ATTENDANCE', (err, data) => {
      if (err) {
        console.log(err)
        res.status(500).json({ message: 'Internal server error' })
      }
      if (data) {
        res.send({ data })
      } else {
        res.status(204).json({ message: 'No attendance in database' })
      }
    })
  }
});


// Redirect all other routes to the Vue.js app
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

// Start the server
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});