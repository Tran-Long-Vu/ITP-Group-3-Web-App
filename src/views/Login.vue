<template >
  <div class="login-container">
    <form @submit.prevent="login">
      <div class="container">
        <div class="border"></div>	
            <div class="login-box">
              <br>
              <br>
              <br>  
              <h1>Welcome!</h1>
              <br>
              <input class="username-box" type="text" name="email" placeholder="Email" v-model="email"><br>
              <br><input type="text" name="password" placeholder="Password" v-model="password" ><br>
              <br><button type="submit">Login</button>
            </div>
        <img src="../assets/orangebg.jpg" alt="Img">
      </div>
    </form>
  </div>
</template>


<script>

 import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    login: function() {
      axios.post('http://localhost:3000/login', {
        email: this.email,
        password: this.password
      }).then(res => {
        const userData = res.data.userData;
        if (userData) {
          this.$store.commit('SET_USER', userData);
          localStorage.user = JSON.stringify(userData); //  vuex into local.
          
          // Login successful, redirect to Home page
          this.$router.push({ name: 'Home' });
        } else {

          // Login failed, display error message
          this.$notify({
            title: 'Error',
            text: 'Invalid email or password',
            type: 'error'
            
          });
        }
      }).catch(error => {
        console.error(error);
        this.$notify({
          title: 'Error',
          text: 'Internal server error',
          type: 'error'
        });
      });
    }
  }
}

</script>

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
  top: 15px;
  left: 0px;
  width: 400px;
  height: 780px;
  margin-top: 10px;
  
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

