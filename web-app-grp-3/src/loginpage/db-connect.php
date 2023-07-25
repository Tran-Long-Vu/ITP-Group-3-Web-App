<?php
$servername = "feenix-mariadb.swin.edu.au";
$username = "s103426463";
$password = "101202";
$dbname = "s103426463_db";

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>