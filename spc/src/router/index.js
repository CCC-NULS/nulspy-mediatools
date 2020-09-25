import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  // mode: 'hash',   hash is default
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../components/HomePage'),
      children: [
        {
          name: 'AllReviews',
          path: '/allreviews',
          component: () => import('../components/AllReviews')
        },
      ]
    }
  ]
})
