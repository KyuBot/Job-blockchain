import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
import actions from './actions'
import mutations from './mutations'

const state = {
  isLogin: false,
  authToken: '',
  isLoggedIn: false,
  signUpInput: '',
  mailCode: '',
  mailValid: false,
  loginPath: '',
}

Vue.use(Vuex)

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
