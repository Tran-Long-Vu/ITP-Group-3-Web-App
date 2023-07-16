<template>
    <div>
      <!-- Navigation bar component -->
      <nav class="navbar navbar-expand-lg navbar-dark bg-warning fixed-top">
        <a class="navbar-brand" href="#">My App</a>
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/calendar">Calendar</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/admin">Admin</router-link>
            </li>
          </ul>
        </div>
      </nav>
  
      <!-- Main content -->
      <div class="container mt-5">
        <h1>{{ userName }}</h1>
        <p>{{ userStatus }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "IndexPage",
    data() {
      return {
        userName: "John Doe",
        userStatus: "Active"
      };
    }
  };
  </script>
  
  <style scoped>
  .navbar-brand {
    font-weight: bold;
  }
  </style>