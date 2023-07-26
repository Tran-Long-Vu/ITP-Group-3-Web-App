<template>
  <div id="app">
    <nav class="navbar">
      <div class="navbar-logo">
        <img src="/logo.jpg" alt="Logo">
      </div>
      <div class="navbar-links">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/Calendar" class="nav-link">Calendar</router-link>
        <button class="nav-link">LOG OUT</button>
        
      </div>
    </nav>
    <div class="content">
      <div class="square"> 
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
    }
  },
  metaInfo: {
    title: 'Home',
  },
}
</script>

