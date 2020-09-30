import Vue from 'vue'
import vuetify from './plugins/vuetify'
import store from './store'
import router from './router'
import App from './App.vue'
import 'material-icons'

new Vue({
  vuetify,
  store,
  router,
  render: h => h(App),
}).$mount('#app')
