<template>
  
  <div id="app">
    <nav class="navbar">
      <div class="navbar-logo">
        <router-link to="/Home">
          <img src="../assets/logo.jpg" alt="Logo" width="120" height="50" style="margin-left: 50px;">
        </router-link>  
      </div>
      <div class="navbar-links">
        <router-link to="/Home" class="nav-link">Home</router-link>
        <router-link to="/Calendar" class="nav-link">Calendar</router-link>
        <button @click="logout">Logout</button>

      </div>
    </nav>
    <!-- Contents of Home  -->    
    <div class="background-square">
      <br>
      <h1 v-if="user"> Welcome, {{ user.name  }} </h1>     <!-- this gets killed upon refresh,.  -->    

      <br>
      <table class="table">
        <tbody>
          <tr>
            <td rowspan="4" :style="{ verticalAlign: 'middle', paddingRight: '20px' }">
              <img src="../assets/profile.jpg" alt="Logo" width="170" height="170" >
            </td>
            <td :style="{ paddingBottom: '10px' }"><h3>Attendance today:</h3></td>
            <td :style="{ paddingBottom: '10px' }"><h3 v-if="user" >Present</h3></td>
          </tr>
          
          <tr>
            <td :style="{ paddingBottom: '10px' }"><h3>Account type:</h3></td>
            <td :style="{ paddingBottom: '10px' }"><h3 v-if="user" >{{ user.admin === 1 ? "Administrator" : "User"}}</h3></td>
          </tr>
          <tr>
            <td :style="{ paddingBottom: '10px' }"><h3>Staff ID:</h3></td>
            <td :style="{ paddingBottom: '10px' }"><h3 v-if="user" >{{ user.UID }}</h3></td>
          </tr>
          <tr>
            <td :style="{ paddingBottom: '10px' }"><h3>Department:</h3></td>
            <td :style="{ paddingBottom: '10px' }"><h3 v-if="user" >{{ user.department }}</h3></td>
          </tr>
          <tr>

          </tr>
        </tbody>
      </table>
    </div>      
  </div>
</template>

<script>
export default {
  
  
  data() {
  return {
    user: null  // JSON.parse(localStorage.user)
  };
},
  
  mounted() {
  const storedUserData = localStorage.user;
  if (storedUserData) {
    this.user = JSON.parse(storedUserData);
  } 
  else {
    // Set default user data if localStorage is empty
    this.$router.push({ name: 'Login' });
    }
  },
  methods: {
    logout() {
      // Clear the local storage
      localStorage.clear();
      this.$router.push({ name: 'Login' });
    }
  }
}
  
  


</script>

<style>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #FFA500; /* Change the background color to FFA500 */
  margin: 0;
  padding: 0;
   
}

.navbar-logo {
  margin-right: 10px;
}

.navbar-links {
  display: flex;
  align-items: center;
  margin-left: 50px;
  margin-right: 50px;
}

.nav-link {
  margin-left: 10px;
}

.background-square {
  background-color: #D9D9D9;
  padding-left: 50px;
  padding-right: 50px;
  min-height: 100vh; /* Set height to 100% of the viewport height */
  height: fit-content;
  margin-left: 50px;
  margin-right: 50px;

}


.table {
  border-collapse: separate;
  border-spacing: 0 0px;
}

.table td {
  padding: 5px;
}

.table td:first-child {
  vertical-align: middle;
  padding-right: 10px;
}

</style>