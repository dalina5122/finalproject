import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import { createRouter, createWebHistory } from 'vue-router'

import DogsMap from './components/DogsMap.vue'
import SignUp from './components/SignUp.vue'
import LogIn from './components/LogIn.vue'
import Layout from './components/Layout.vue'
import Index from './components/Index.vue'
import CatsMap from './components/CatsMap.vue'
import Profile from './components/Profile.vue'

const routes=[
  {path: '/', component: Layout, children:[
    {path: '', component: Index},
    {path: '/signup', component: SignUp},
    {path: '/dogsmap', component: DogsMap},
    {path: '/log-in', component: LogIn},
    {path: '/catsmap', component: CatsMap},
    {path: '/profile', component: Profile}
  ]}
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URLs),
  routes
})

createApp(App).use(router).mount('#app')