<template>
   <div id="app">
    <nav class="navbar ">
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
    <!-- Contents -->
    <div class="background-square">
      <br>
    <div class="main-title">
      <h1>Calendar</h1>
    </div>    
    <div class="btn-container">
      <button class="prev-btn" @click="prevMonth">Prev  </button>
      <h1 colspan="7">{{ monthNames[currentMonth] }} {{ currentYear }}</h1>
      <button class="next-btn" @click="nextMonth">Next</button>
    </div>
    <br>
    <table>
      <thead>
        <tr>
          
        </tr>
        <tr>
          <th>Sun</th>
          <th>Mon</th>
          <th>Tue</th>
          <th>Wed</th>
          <th>Thu</th>
          <th>Fri</th>
          <th>Sat</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(week, index) in weeks" :key="index">
          <td v-for="(day, index) in week" :key="index">
            <button class="day-btn" :id="'day-' + day + '-' + currentMonth" :class="{ 'red': !attendance[day] }" @click="handleDayClick(day)">{{ day }}</button>
          </td>
          
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
      currentYear: new Date().getFullYear(),
      currentMonth: new Date().getMonth(),
      monthNames: [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December',
      ],
      weeks: [],
      selectedDay: null,
      attendance: {},
    };
  },
  mounted() {
    this.updateTable();
    this.setAttendance();
  },
  methods: {
    updateTable() {
      const daysInMonth = new Date(this.currentYear, this.currentMonth + 1, 0).getDate();
      const firstDayOfMonth = new Date(this.currentYear, this.currentMonth, 1).getDay();
      const lastDayOfMonth = new Date(this.currentYear, this.currentMonth, daysInMonth).getDay();
      
      const weeks = [[]];
      let currentWeek = 0;
      let currentDay = 1;
      for (let i = 0; i < firstDayOfMonth; i++) {
        weeks[currentWeek].push(null);
      }
      while (currentDay <= daysInMonth) {
        if (weeks[currentWeek].length === 7) {
          currentWeek++;
          weeks.push([]);
        }
        weeks[currentWeek].push(currentDay);
        currentDay++;
      }
      for (let i = lastDayOfMonth; i < 6; i++) {
        weeks[currentWeek].push(null);
      }
      
      this.weeks = weeks;
    },
    calculateAttendanceCount() {
    const attendance = this.attendance;
    this.weeks.forEach((week) => {
      week.forEach((day) => {
        if (day.day !== null) {
          const yearMonthDay = `${this.currentYear}-${this.currentMonth + 1}-${day.day}`;
          if (attendance[yearMonthDay]) {
            day.isAttended = true;
            
          }
        }
      });
    });
  },
    prevMonth() {
      this.currentMonth = (this.currentMonth - 1 + 12) % 12;
      if (this.currentMonth === 11) {
        this.currentYear--;
      }
      this.updateTable();
      this.calculateAttendanceCount();
      
    },
    nextMonth() {
      this.currentMonth = (this.currentMonth + 1) % 12;
      if (this.currentMonth === 0) {
        this.currentYear++;
      }
      this.updateTable();
      this.calculateAttendanceCount();
    },
    handleDayClick(day) {
      if (day.isCurrentMonth) {
        this.selectedDay = day.day;
      }
    },
  },
};
</script>


<style scoped>
.main-title{
  text: center;
}
button {
  display: block;
  width: 100%;
  height: 100%;
  padding: 10px;
  font-size: 16px;
  font-weight: bold;
  text-align: center;
  background-color: #f2f2f2;
  border: none;
  border-radius: 0;
  cursor: pointer;
}

button:hover {
  background-color: #ddd;
}

button:active {
  background-color: #ccc;
}
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
.btn-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.prev-btn, .next-btn {
  background-color: #FFA500;
  color: FFFFFF;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 1px 20px;
  cursor: pointer;
  width: 100px;
  border-radius: 8px;

}

h2 {
  margin: 0;
  font-size: 20px;
}
/* Style the calendar table */
table {
      border-collapse: collapse;
      margin: auto;
      width: 100%;
    }
    th, td {
      border: 1px solid black;
      padding: 10px;
    }
    th {
      background-color: #ccc;
    }
    td {
      text-align: center;
    }
    .red {
      background-color: #FF6347;
      color: #fff;
    }

    .day-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  outline: none;
  font-size: 16px;
  font-weight: bold;
}

.gray {
  color: #ccc;
}

.red {
  background-color: #FF6347;
  color: white;
}
.day-tile.is-attended {
  background-color: #FFA500;
}

</style>