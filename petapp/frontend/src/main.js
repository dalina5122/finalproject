import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import { createRouter, createWebHistory } from 'vue-router'

import DogsMap from './components/DogsMap.vue'
import SignUp from './components/SignUp.vue'
import LogIn from './components/LogIn.vue'


// createApp(App).mount('#app')

const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: '/', component: SignUp },
      { path: '/dogs-map', component: DogsMap },
      { path: '/log-in', component: LogIn }
    ]
  })
  
  createApp(App).use(router).mount('#app')