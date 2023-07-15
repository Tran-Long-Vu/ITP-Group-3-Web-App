import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'

import Frames from './views/frames'
import './style.css'

Vue.use(Router)
Vue.use(Meta)
export default new Router({
  mode: 'history',
  routes: [
    {
      name: 'Frames',
      path: '/',
      component: Frames,
    },
  ],
})
