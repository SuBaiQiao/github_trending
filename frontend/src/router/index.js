import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('@/components/RepoTable.vue')
    },
    {
      path: '/settings',
      name: 'Settings',
      component: () => import('@/components/SettingPage.vue')
    }
  ] 
})

export default router