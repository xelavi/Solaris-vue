import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Character from '@/views/Character.vue'
import CreateCharacter from '@/views/CreateCharacter.vue'
import Arbol from '@/views/Arbol.vue'
import Background from '@/views/Background.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/:character_slug/',
    name: 'Character',
    component: Character
  },
  {
    path: '/create-character/',
    name: 'CreateCharacter',
    component: CreateCharacter
  },
  {
    path: '/create-character/arbol',
    name: 'Arbol',
    component: Arbol
  },
  {
    path: '/create-character/background',
    name: 'Background',
    component: Background
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
