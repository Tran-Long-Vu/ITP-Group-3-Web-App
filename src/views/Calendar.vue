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
        <button @click="logout">Logout</button>
      </div>
    </nav>
    <!-- Contents -->
    <div class="background-square">
      <br>
      <div class="main-title">
        <h1>Calendar</h1>
      </div>
      <br>
      <div class="leg-container">
        <span class="date-text">{{ currentDate.toLocaleDateString("en-US", { year: 'numeric', month: 'long' }) }}</span>
        <div class="date-picker-container">
          <button v-on:click="showDatePicker = !showDatePicker" class="cal-btn">Calendar</button>
          <div>
            <date-picker :value="currentDate" @input="handleCalendarInput" :inline="true" minimum-view="month"
              maximum-view="month" v-if="showDatePicker"></date-picker>
          </div>
        </div>
      </div>
      <div class="pagination-container">
        <paginate v-model="currentPage" :page-count="pages" :page-range="9" :click-handler="clickHandler"
          :prev-text="'Previous'" :next-text="'Next'" :container-class="'pagination'">
        </paginate>
      </div>
      <div class="container">
        <table>
          <thead>
            <tr>
              <th>Day</th>
              <th v-for="day in slicedDay" :key="day">{{ day }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="staff in staffData">
              <td>{{ staff.name }}</td>
              <td v-for="day in slicedDay" :key="day + staff.UID" @mouseenter="handleMouseEnter(day)"
                @mouseleave="handleMouseLeave(day)">
                <div v-if="getAttendanceStatus(day, staff.UID) !== ''" class="attendance-cell"
                  :class="getAttendanceStatus(day, staff.UID) === 'Attended' ? 'yes-status' : 'no-status'">
                  {{ getAttendanceStatus(day, staff.UID) }}
                  <span v-if="getAttendanceStatus(day, staff.UID) === 'Attended'" class="attendance-time">
                    {{ getAttendanceTime(day, staff.UID) }}
                  </span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>



<script>
import Paginate from 'vuejs-paginate'
import Datepicker from 'vuejs-datepicker';
import axios from 'axios';

export default {
  data() {
    return {
      staffData: [],
      attendanceData: [],
      hoveredCell: null,
      pageSize: 7,
      currentPage: 1,
      currentMonth: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      showDatePicker: false,
      datePicker: null
    };
  },
  methods: {
    getAttendanceStatus(day, staffId) {
      const entry = this.attendanceData.find(
        data => new Date(data.Timestamp).getDate() === day && new Date(data.Timestamp).getMonth() === this.currentMonth && data.UID === staffId
      );
      if (entry) {
        return entry.Status === 1 ? "Attended" : "Absent"
      }
      return ""
    },
    getAttendanceTime(day, staffId) {
      const entry = this.attendanceData.find(
        data => new Date(data.Timestamp).getDate() === day && new Date(data.Timestamp).getMonth() === this.currentMonth && data.UID === staffId
      );
      return entry ? new Date(entry.Timestamp).toLocaleTimeString("en-US", { timeStyle: "medium" }) : "";
    },
    handleMouseEnter(day) {
      this.hoveredCell = day;
    },
    handleMouseLeave(day) {
      this.hoveredCell = null;
    },
    showAttendanceTime(day) {
      return this.hoveredCell === day;
    },
    clickHandler: function (pageNum) {
      this.currentPage = pageNum;
    },
    handleCalendarInput(input) {
      this.currentPage = 1
      this.currentMonth = input.getMonth()
      this.currentYear = input.getFullYear()
    },
    logout() {
      // Clear the local storage
      localStorage.clear();
      this.$router.push({ name: 'Login' });
    }
  },
  components: {
    'paginate': Paginate,
    'date-picker': Datepicker
  },
  computed: {
    pages: function () {
      return Math.ceil(this.dateCount / this.pageSize)
    },
    dateCount: function () {
      return new Date(new Date().getFullYear(), this.currentMonth, 0).getDate()
    },
    slicedDay: function () {
      const startIndex = this.pageSize * (this.currentPage - 1);
      const endIndex = startIndex + this.pageSize;
      return this.days.slice(startIndex, endIndex);
    },
    days: function () {
      return Array.from({ length: this.dateCount }, (_, i) => i + 1)
    },
    currentDate: function () {
      return new Date(this.currentYear, this.currentMonth)
    }
  },
  mounted() {
    axios.get('http://localhost:3000/calendars/users').then(res => {
       this.staffData = res.data.data
    })
    axios.get('http://localhost:3000/calendars/attendance').then(res => {
       this.attendanceData = res.data.data
    })
  }
};
</script>

<style scoped>
.main-title {
  text-align: center;
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

.attendance-cell {
  min-width: 60px;
  width: 100%;
  padding: 6px;
  border-radius: 5px;
  text-align: center;
  margin: auto;
}

.yes-status {
  background-color: rgb(49, 204, 49);
}

.no-status {
  background-color: rgb(196, 0, 0);
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

.prev-btn,
.next-btn {
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



.container {
  width: 100%;
  height: 80vh;
  /* Set the width of the container */
  overflow-x: auto;
  /* Enable horizontal scrolling */
  overflow-y: auto;
  /* Hide vertical scrolling */
  direction: rtl;
  /* Reverse the direction of content */
}

.container::-webkit-scrollbar-track {
  background-color: #F5F5F5;
}

.container::-webkit-scrollbar {
  width: 5px;
  background-color: #F5F5F5;
}

.container::-webkit-scrollbar-thumb {
  background-color: #000000;
  border: 2px solid #555555;
}

table {
  width: fit-content;
  margin: auto;
  /* Set the table to adjust its width based on content */
  white-space: nowrap;
  /* Prevent line breaks within table cells */
  direction: ltr;
  /* Restore the normal direction of content */
}

/* Additional styles for the table, cells, and headers (adjust as needed) */
table {
  border-collapse: collapse;
}

th,
td {
  min-width: 60px;
  height: 30px;
  padding: 6px;
  border: 1px solid black;
}

th {
  background-color: #f2f2f2;
  text-align: left;
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
  background-color: #FF8D79;
  color: white;
}

.day-tile.is-attended {
  background-color: #FFA500;
}

.pagination>li>a,
.pagination>li>span {
  position: relative;
  float: left;
  padding: 6px 12px;
  margin-left: -1px;
  line-height: 1.42857143;
  color: #337ab7;
  text-decoration: none;
  background-color: #fff;
  border: 1px solid #ddd;
}
</style>

<!-- Pagination style -->
<style>
.pagination>li {
  display: inline;
}

.pagination {
  padding-left: 0;
  margin: 20px;
  border-radius: 4px;
}

.pagination>.active>a,
.pagination>.active>span,
.pagination>.active>a:hover,
.pagination>.active>span:hover,
.pagination>.active>a:focus,
.pagination>.active>span:focus {
  z-index: 2;
  color: #fff;
  cursor: default;
  background-color: #337ab7;
  border-color: #337ab7;
}

.pagination>.disabled>span,
.pagination>.disabled>span:hover,
.pagination>.disabled>span:focus,
.pagination>.disabled>a,
.pagination>.disabled>a:hover,
.pagination>.disabled>a:focus {
  color: #949494;
  cursor: not-allowed;
  border-color: #ddd;
}

.pagination a {
  color: black;
  float: left;
  padding: 8px 16px;
  text-decoration: none;
  transition: background-color .3s;
  border: 1px solid #8d8d8d;
  margin: 5px 3px;
}

.pagination-container {
  width: fit-content;
  margin: auto;
}

.date-text {
  text-align: center;
  font-size: 25px;
}

.leg-container {
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 10px;
}

.date-picker-container {
  width: fit-content;
  display: flex;
}

.cal-btn {
  margin-left: 100px;
  width: fit-content;
  height: fit-content;
  padding: 10px;
  margin: 0px 10px;
  font-size: 16px;
  font-weight: bold;
  text-align: center;
  background-color: #FFA500;
  cursor: pointer;
  border-radius: 10px
}
</style>