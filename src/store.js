import Vuex from "vuex"
import Vue from 'vue'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const store = new Vuex.Store({
  plugins: [createPersistedState({
    storage: window.sessionStorage,
})],
  state() {
    return {
      // Define your initial state here
      count: 0,
      isLoggedIn: false,
      user: null
    }
  },
  mutations: {
    // Define your mutations here
    SET_USER(state, user) {
      state.user = user;
    },
    setIsLoggedIn (state, value) {
      state.isLoggedIn = value
    },
    setUser (state, user) {
      state.user = user
    }
  },
  actions: {
    // Define your actions here
    login ({ commit }, userData) {
      // Call your API to authenticate the user here
      // Then commit the setIsLoggedIn and setUser mutations
      commit('setIsLoggedIn', true)
      commit('setUser', userData)
    },
    logout ({ commit }) {
      // Call your API to log out the user here
      // Then commit the setIsLoggedIn and setUser mutations
      commit('setIsLoggedIn', false)
      commit('setUser', null)
    }
  },
  getters: {
    GET_USER: state => {
      return state.user; // return data
    }
  }
})

export default store;
