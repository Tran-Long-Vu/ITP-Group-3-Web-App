import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'
import Login from './views/Login.vue'
import Home from './views/Home.vue'
import Calendar from './views/Calendar.vue'
import './style.css'

Vue.use(Router)
Vue.use(Meta)
export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/Login'
    },
    {
      name: 'Login',
      path: '/Login',
      component: Login,
    },
    {
      name: 'Home',
      path: '/Home',
      component: Home,
    },
    {
      name: 'Calendar',
      path: '/Calendar',
      component: Calendar,
    },
    
  ],
})