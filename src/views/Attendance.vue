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
        <router-link to="/Login" class="nav-link">LOG OUT</router-link>
      </div>
    </nav>
    <!-- Contents of Attendance  -->
    <div class="content">
      <div class="square"> 
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'attendance',
  data() {
    return {
    }
  },
  metaInfo: {
    title: 'Attendance project',
  },
}
</script>