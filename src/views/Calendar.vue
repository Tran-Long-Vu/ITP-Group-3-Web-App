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
        <router-link to="/Login" class="nav-link">Logout</router-link>
      </div>
    </nav>
    <!-- Contents of Cal  -->
    
    <div class="background-square">
      <br>
      <h1>Calendar</h1>
      <br>
      <div class="calendar-nav">
        <div class="calendar-nav">
          <button id="prev-btn">Prev</button>
          <h2 id="month">July</h2>
          <button id="next-btn">Next</button>
          <h2>Monthly view</h2>
        </div>
      </div>
      <br>
      <table class="calendar">
        <thead>
          <tr>
            <th v-for="day in daysOfWeek">{{ day }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(week, index) in weeks" :key="index">
            <td v-for="day in week" :class="{ today: isToday(day), selected: isSelected(day) }" @click="selectDate(day)">
              {{ day.getDate() }}
            </td>
          </tr>
        </tbody>
      </table>
    </div> 
      
      <!-- Rest of your content here -->
    
  </div>
</template>
<script>
export default {
  name: 'Calendar',
  data() {
    return {
      selectedDate: null,
      daysOfWeek: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      weeks: [],
      months: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      currentMonth: new Date().getMonth()
    }
  },
  methods: {
    isToday(date) {
      const today = new Date()
      return date.toDateString() === today.toDateString()
    },
    isSelected(date) {
      return date.toDateString() === this.selectedDate?.toDateString()
    },
    selectDate(date) {
      this.selectedDate = date
      this.$emit('select-date', date)
    },
    prevMonth() {
      this.currentMonth--;
      if (this.currentMonth < 0) {
        this.currentMonth = 11; // December is the 12th month
      }
    },
    nextMonth() {
      this.currentMonth++;
      if (this.currentMonth > 11) {
        this.currentMonth = 0; // January is the 1st month
      }
    }
  },
  mounted() {
    const today = new Date()
    const startOfMonth = new Date(today.getFullYear(), this.currentMonth, 1)
    const endOfMonth = new Date(today.getFullYear(), this.currentMonth + 1, 0)
    const daysInMonth = endOfMonth.getDate()
    const dayOfWeek = startOfMonth.getDay()
    let date = 1;
    let week = [];
    for (let i = 0; i < 7; i++) {
      if (i < dayOfWeek) {
        week.push(null);
      } else {
        week.push(new Date(today.getFullYear(), this.currentMonth, date));
        date++;
      }
    }
    this.weeks.push(week);

    while (date <= daysInMonth) {
      week = [];
      for (let i = 0; i < 7; i++) {
        if (date > daysInMonth) {
          week.push(null);
        } else {
          week.push(new Date(today.getFullYear(), this.currentMonth, date));
          date++;
        }
      }
      this.weeks.push(week);
    }
  }
}
</script>

<style scoped>
.calendar {
  border-collapse: collapse;
  width: 100%;
  border: 1px solid black;
}

.calendar td {
  border: 1px solid black;
  padding: 10px;
  text-align: center;
}

.calendar td.today {
  font-weight: bold;
}

.calendar td.selected {
  background-color: #007bff;
  color: #fff;
}

.calendar td:hover {
  cursor: pointer;
  background-color: #f0f0f0;
}
.calendar-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #f0f0f0;
}

.prev-btn, .next-btn {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

h2 {
  margin: 0;
  font-size: 20px;
}
</style>