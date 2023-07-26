<template >
    <div class="login-container">
      <form>
        <div class="container">
          <div class="border"></div>	
              <div class="login-box">
                <br>
                <br>
                <br>
                
                <h1>Welcome!</h1>
                <br>
                <input class="username-box" type="text" placeholder="Username"><br>
                <br><input type="text" placeholder="Password"><br>
                <br><button type="submit" >Login</button>
              </div>
          <img src="../assets/orangebg.jpg" alt="Img">
        </div>
      </form>
    </div>
  </template>

<style scoped>
.login-container {
  display: flex;
  flex-direction: row;
  height: 100vh;
}



.login-image {
  width: 66.67%;
  
  
}
.login-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
}

.login-image img {
  max-width: 100%;
  max-height: 100%;
}
body {
  margin: 10px 10px 10px 0px;
  padding: 0;
  font-family: Arial, sans-serif;

}
.login-box {
    position: absolute;
    top: 170px;
    left: 1px;
    width: 500px;
    padding: 50px;
    font-family: Arial, sans-serif;
    
}
img{
  width: 100%;
  height: 100%;
  background-size: contain;

}

.border {
  position: absolute;
  top: -15px;
  left: 0px;
  width: 400px;
  height: 780px;
  padding: 100px;
  background-color: white;
	border-radius: 0px 100px 100px 00px;
}

h1 {
  text-align: left;
	font-size: 65px ;
  margin-top: -15vh; /* Adjust this value as needed */

}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
}

input {
	margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 60%;
	padding: 15px;
}
username-box{
margin-top: 0px;
}
button {
  padding: 10px 20px 10px 20px;
  background-color: #FFA550;
  color: #222222;
  border: none;
  border-radius: 20px 20px 20px 20px;
  cursor: pointer;
  width: 25%;
}

.error-text {
  color: red;
  text-align: center;
}

.shape {
  width: 0;
  height: 0;
  border-left: 50px solid transparent;
  border-right: 50px solid transparent;
  border-top: 100px solid #007BFF;
  margin: 20px auto;
}

</style>

