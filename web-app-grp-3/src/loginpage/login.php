<?php
// Include the database connection file
require_once "db-connect.php";
?>

<!DOCTYPE html>
<html>
<head>
  
<title>Log-in Site</title>
<link rel="stylesheet" href="login.css">
  <!-- Add the Vue.js library -->
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>

</head>

<body>
<form>
<div class="container">
	<div class="border"></div>
	<div class="loginbox">
		<h1>Welcome!</h1>
		  <input type="text" placeholder="Username"><br>
			<br><input type="text" placeholder="Password"><br>
			<br><button type="submit">Login</button>
	</div>	
</div>
</form>
	
</body>
</html>
