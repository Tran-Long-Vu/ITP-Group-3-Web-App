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
    
    <br>
    <table>
      <thead>
        <tr>
          <th>Day</th>
          <th v-for="staff in staffNames" :key="staff.id">{{ staff.name }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="day in days" :key="day">
          <td>{{ day }}</td>
          <td v-for="staff in staffNames" :key="staff.id" @mouseenter="handleMouseEnter(day, staff.id)" @mouseleave="handleMouseLeave(day, staff.id)">
            <div :style="{ backgroundColor: getAttendanceColor(day, staff.id) }" class="attendance-cell">
              {{ getAttendanceStatus(day, staff.id) }}
              <div v-if="showAttendanceTime(day, staff.id)" class="attendance-time-box">
                {{ getAttendanceTime(day, staff.id) }}
              </div>
            </div>
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
      days: Array.from({ length: 31 }, (_, i) => i + 1), // Array of days from 1 to 31
      staffNames: [
        { id: 1, name: "John Doe" },
        { id: 2, name: "Jane Smith" },
        { id: 3, name: "Michael Johnson" },
        { id: 4, name: "Emily Davis" },
        { id: 5, name: "David Wilson" }
      ],
      attendanceData: [
        { day: 1, staffId: 1, status: "Yes", time: "09:00 AM" },
        { day: 1, staffId: 2, status: "No", time: "" },
        { day: 1, staffId: 3, status: "Yes", time: "10:30 AM" },
        { day: 1, staffId: 4, status: "Yes", time: "11:15 AM" },
        { day: 1, staffId: 5, status: "No", time: "" },
        // Add more entries for the remaining days and staff members
      ],
      hoveredCell: { day: null, staffId: null }
    };
  },
  methods: {
    getAttendanceStatus(day, staffId) {
      const entry = this.attendanceData.find(
        data => data.day === day && data.staffId === staffId
      );
      return entry ? entry.status : "";
    },
    getAttendanceColor(day, staffId) {
      const status = this.getAttendanceStatus(day, staffId);
      return status === "Yes" ? "green" : "#FF735A";
    },
    getAttendanceTime(day, staffId) {
      const entry = this.attendanceData.find(
        data => data.day === day && data.staffId === staffId
      );
      return entry ? entry.time : "";
    },
    handleMouseEnter(day, staffId) {
      this.hoveredCell.day = day;
      this.hoveredCell.staffId = staffId;
    },
    handleMouseLeave(day, staffId) {
      this.hoveredCell.day = null;
      this.hoveredCell.staffId = null;
    },
    showAttendanceTime(day, staffId) {
      return this.hoveredCell.day === day && this.hoveredCell.staffId === staffId;
    }
  }
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

.attendance-cell {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 30px; /* Adjusted height to make the cell smaller */
  width: 30px; /* Adjusted width to make the cell smaller */
  border-radius: 10px;
  z-index: 1;
}

.attendance-time-box {
  position: absolute;
  top: 50%;
  left: calc(100% + 10px); /* Adjusted the left position to create a gap between the tile and the box */
  transform: translateY(-50%);
  background-color: white;
  padding: 5px;
  border: 2px solid black;
  display: inline-block;
  border-radius: 5px;
  z-index: 2;
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
      background-color: #FF8D79;
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
  background-color: #FF8D79;
  color: white;
}
.day-tile.is-attended {
  background-color: #FFA500;
}

</style>