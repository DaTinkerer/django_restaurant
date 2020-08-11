import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home'
import Menu from '@/components/Menu'
// import Sand from '@/components/Sand'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },

  {
    path: '/menu',
    name: 'Menu',
    component: Menu
  },
  // {
  //   path: '/sandwiches',
  //   name: 'Sand',
  //   component: Sand
  // },
  
]

const router = new VueRouter({
  routes
})

export default router
