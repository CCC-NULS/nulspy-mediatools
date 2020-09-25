import Vue from 'vue'
import Vuex from 'vuex'
// import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    gHomeKeyCount: 0,
    gShowHomeBool: true,
    gShowAllrevs: false,
    gMobile: false,
  },
  mutations: {
    gHomeKeyCountMut(state, theval) {
      state.gHomeKeyCount = theval
    },
    gShowHomeBoolMut(state, theval) {
      state.gShowHomeBool = theval
    },
    gShowAllrevsMut(state, theval) {
      state.gShowAllrevs = theval
    },  
    gMobileMut(state, theval) {
      state.gMobile = theval
    },     
  },
  getters: {
    getShowAllrevs: state => state.gShowAllrevs,
    getShowHomeBool: state => state.gShowHomeBool,
  },
  actions: {
    gHomeKeyCountAct(context, theval) {
      context.commit('gHomeKeyCountMut', theval)
    },    
    gShowHomeBoolAct(context, theval) {
      context.commit('gShowHomeBoolMut', theval)
    },
    gShowAllrevsAct(context, theval) {
      context.commit('gShowAllrevsMut', theval)
    },
    gMobileAct(context, theval) {
      context.commit('gMobileMut', theval)
    },    
  },
  modules: {
  }
})
