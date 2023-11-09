import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import userView from '@/views/userView.vue'
import LoginView from '@/views/LoginView.vue'

const isAuthenticated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/user/:id', 
      name: 'user',
      component: userView,
    },
    {
      path: '/login', 
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('이미 로그인 되어 있습니다.')
          return { name : 'home' }
        }
      }
    }
  ]
})

// router.beforeEach((to, from) => {
//   console.log(to)
//   console.log(from)
//   const isAuthenticated = false
  
//   if (!isAuthenticated && to.name !== 'login') {
//     console.log('로그인이 필요합니다.')
//     return { name: 'login'}
//   }
// })

router.beforeEach((to, from) => {
  console.log(to)
  console.log(from)
})

export default router
