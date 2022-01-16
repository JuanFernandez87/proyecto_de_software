import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Router being imported

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import "leaflet/dist/leaflet.css"

import PrimeVue from 'primevue/config'
import Button from 'primevue/button'
import Menubar from 'primevue/menubar';
import Card from 'primevue/card';
import Vuelidate from 'vuelidate'

import 'primevue/resources/themes/saga-blue/theme.css'       //theme
import 'primevue/resources/primevue.min.css'                 //core css
import 'primeicons/primeicons.css'                           //icons

const app = createApp(App);
app.use(PrimeVue);
app.use(Menubar);
app.use(Card);
app.use(Vuelidate);

app.component('Button', Button);
app.component('Menubar', Menubar);
app.component('Card', Card);

app.use(router).mount('#app')
