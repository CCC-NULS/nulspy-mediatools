import Vue from 'vue'
import vuetify from './plugins/vuetify'
import store from './store'
import router from './router'

import App from './App.vue'
import 'material-icons'
// import colors from 'vuetify/lib/util/colors'

Vue.config.productionTip = true

new Vue({
  vuetify,
  store,
  router,
  render: h => h(App)
}).$mount('#app')
// nms: perfect
// colors,
// iconfont: 'mdi',
