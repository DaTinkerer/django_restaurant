import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home'
import Menu from '@/components/Menu'
import Nutrition from '@/components/Nutrition' 

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
   {
     path: '/nutrition',
     name: 'Nutrition',
     component: Nutrition
   },
  
]




const router = new VueRouter({
  routes
  
})

export default router
