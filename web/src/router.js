import { createRouter, createWebHistory } from 'vue-router'
import Carga_denuncias from './views/Carga_denuncias.vue'
import Denuncias_Detalle from './views/Denuncias_Detalle.vue'
import Home from './views/Home.vue'
// import Puntos_encuentro from './views/Puntos_encuentro.vue'
//import Recorridos_evacuacion from './views/Recorridos_evacuacion.vue'
import Recorridos_puntos from './views/Recorridos_puntos.vue'
import Registro_usuario from './views/Registro_usuario.vue'
import Zonas_inundables from './views/Zonas_inundables.vue'
import Zona_Inundable_Detalle from './views/Zona_Inundable_Detalle'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/carga_denuncias',
    name: 'carga_denuncias',
    component: Carga_denuncias
  },
  {
    path: '/denuncias/all',
    name: 'denuncias',
    component: Denuncias_Detalle,
  },  
  {
    path: '/recorridos_puntos',
    name: 'recorridos_puntos',
    component: Recorridos_puntos
  },
  {
    path: '/registro_usuario',
    name: 'registro_usuario',
    component: Registro_usuario
  },
  {
    path: '/zonas_inundables',
    name: 'zonas_inundables',
    component: Zonas_inundables
  },
  {
    path: '/zonas_inundables/:zonaId/details',
    name: 'details',
    component: Zona_Inundable_Detalle,
    props: true,
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
