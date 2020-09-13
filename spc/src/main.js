import Vue from 'vue'
import vuetify from './plugins/vuetify'
import store from './store'
import router from './router'
import './plugins/vuetify'
import App from './App.vue'
import 'material-icons'
import colors from 'vuetify/lib/util/colors'

Vue.config.productionTip = false

new Vue({
  vuetify,
  store,
  colors,
  router,
  iconfont: 'mdi',
  render: h => h(App)
}).$mount('#app')
// nms: perfect
