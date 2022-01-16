<template>
<div class="container">
    <h1 class="border-botton-dotted left">Realizar denuncia</h1> 
      <div class="mt-5">  

    <form class="p-fluid" @submit.prevent="handleSubmit(!v$.$invalid)">
              <div class="form-row mb-2">
                    <div class="input-group">
                        <div class="form-group col-md-6 pr-2 left">
                            <div class="input-group mt-2">
                                <div class="form-group col-md-6 pr-2">
                                    <label class="form-label" :class="{'p-error':v$.nombre_denunciante.$invalid && submitted}">Nombre</label>
                                    <input type="text" class="form-control" name="nombre_denunciante" id="nombre_denunciante" aria-describedby="inputGroup-sizing-default" v-model="form.nombre_denunciante"/>
                                    <small v-if="(v$.nombre_denunciante.$invalid && submitted) || v$.nombre_denunciante.$pending.$response" class="p-error">{{v$.nombre_denunciante.required.$message.replace('Value', 'Name')}}</small>
                                </div>
                                
                                <div class="form-group col-md-6 pr-2">
                                    <label class="form-label" :class="{'p-error':v$.apellido_denunciante.$invalid && submitted}">Apellido</label>
                                    <input type="text" class="form-control" name="apellido_denunciante" id="apellido_denunciante" aria-describedby="inputGroup-sizing-default" v-model="form.apellido_denunciante">
                                    <small v-if="(v$.apellido_denunciante.$invalid && submitted) || v$.apellido_denunciante.$pending.$response" class="p-error">{{v$.apellido_denunciante.required.$message.replace('Value', 'Name')}}</small>
                                </div>
                            </div>

                            <div class="input-group mt-3">
                                <div class="form-group col-md-6 pr-2 left">
                                    <label class="form-label" :class="{'p-error':v$.tel_cel_denunciante.$invalid && submitted}">Teléfono de contacto</label>
                                    <input type="text" class="form-control" name="tel_cel_denunciante" id="tel_cel_denunciante" aria-describedby="inputGroup-sizing-default" v-model="form.tel_cel_denunciante">
                                    <small v-if="(v$.tel_cel_denunciante.$invalid && submitted) || v$.tel_cel_denunciante.$pending.$response" class="p-error">{{v$.tel_cel_denunciante.required.$message.replace('Value', 'Name')}}</small>
                                </div>
                                <div class="form-group col-md-6 pr-2">
                                    <label class="form-label" :class="{'p-error':v$.email_denunciante.$invalid && submitted}">Correo electrónico</label>
                                    <input type="email" class="form-control" name="email_denunciante" id="email_denunciante" aria-describedby="emailHelp" v-model="form.email_denunciante">
                                    <small v-if="(v$.email_denunciante.$invalid && submitted) || v$.email_denunciante.$pending.$response" class="p-error">{{v$.email_denunciante.required.$message.replace('Value', 'Name')}}</small>
                                </div>
                            </div>

                            <div class="input-group mt-3">
                                <div class="form-group col-md-6 pr-2 left">
                                    <label class="form-label" :class="{'p-error':v$.titulo.$invalid && submitted}">Titulo</label>
                                    <input type="text" class="form-control" name="titulo" id="titulo" aria-describedby="inputGroup-sizing-default" v-model="form.titulo">
                                    <small v-if="(v$.titulo.$invalid && submitted) || v$.titulo.$pending.$response" class="p-error">{{v$.titulo.required.$message.replace('Value', 'Name')}}</small>
                                </div>

                                <div class="form-group col-md-6 pr-2">
                                    <label class="form-label" :class="{'p-error':v$.categoria.$invalid && submitted}">Categoria</label>
                                    <select class="form-select" v-model="form.categoria">                                
                                        <option value="2">Alcantarilla tapada</option>
                                        <option value="1">Basural</option>
                                    </select>
                                    <small v-if="(v$.categoria.$invalid && submitted) || v$.categoria.$pending.$response" class="p-error">{{v$.categoria.required.$message.replace('Value', 'Name')}}</small>
                                </div>
                    
                            </div>

                            <div class="input-group mt-3">
                                <div class="form-group col-md-12 pr-2 left">
                                    <label class="form-label" :class="{'p-error':v$.descripcion.$invalid && submitted}">Descripción</label>
                                    <input type="text" class="form-control" name="descripcion" id="descripcion" aria-describedby="inputGroup-sizing-default" v-model="form.descripcion">
                                    <small v-if="(v$.descripcion.$invalid && submitted) || v$.descripcion.$pending.$response" class="p-error">{{v$.descripcion.required.$message.replace('Value', 'Name')}}</small>
                                </div>                    
                            </div>
                        </div>
                            
                            <div class="form-group col-md-3 pr-2">
                                <label for="latitud">Coordenadas</label>
                                <div class="input-group">
                                    <input type="text" name="lat" id="lat" v-model="form.latitud">
                                    <input type="text" name="lat" id="lng" v-model="form.longitud">
                                    <div class="map-container">
                                        <div id="mapid">
                                            <l-map @ready="onReady" :zoom="zoom" :center="center" @click="get_point">>
                                                <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>                                                       
                                                <l-marker :lat-lng="markerLatLng" :draggable="true" ></l-marker>
                                            </l-map>
                                        </div>   
                                    </div>
                                </div>
                            </div>

                        
                    </div>
                </div>   
            <div class="form-row mb-2">
                <div class="input-group">
                <div class="form-group col-md-4 pr-2">
                    <a class="btn btn-secondary mt-2 mr-1" v-on:click="cancel()">Cancelar</a>
                    <button class="btn btn-primary mt-2">Guardar</button>
                </div>
                </div>
            </div>
    </form>
</div>
</div>
</template>

<script>
import { LMap, LTileLayer, LMarker } from '@vue-leaflet/vue-leaflet';
import axios from 'axios'
import {required, email, numeric, helpers, alpha} from '@vuelidate/validators'
import useValidate from "@vuelidate/core";
import { reactive, computed, ref } from 'vue'

let lat = -34.921350359799966;
let lng = -57.95456493253922;

export default {
    name: "Carga_denuncias", 
    setup() {
      const form = reactive({
          apellido_denunciante: '',
          categoria: null,
          descripcion: '',
          email_denunciante: '',
          latitud: '',
          longitud: '',
          nombre_denunciante: '',
          tel_cel_denunciante: null,
          titulo: '', 
      })

      const rules = computed(() => {
            return{
            apellido_denunciante: { required: helpers.withMessage("Campo requerido", required), alpha },
            categoria: { required: helpers.withMessage("Campo requerido", required) },
            descripcion: { required: helpers.withMessage("Campo requerido", required) },
            email_denunciante: { required: helpers.withMessage("Campo requerido", required), email },
            nombre_denunciante: { required: helpers.withMessage("Campo requerido", required), alpha },
            tel_cel_denunciante: { required: helpers.withMessage("Campo requerido", required), numeric}, 
            titulo: { required: helpers.withMessage("Campo requerido", required) },
            }
      })
      const submitted = ref(false);
      const showMessage = ref(false);
      const v$ = useValidate(rules, form)
      const handleSubmit = (isFormValid) => {
          submitted.value = true;
          if(!isFormValid){
              alert('Debe completar los campos necesarios')
              return;
          } 
          toggleDialog();
          axios.post(process.env.VUE_APP_API_URL + 'denuncias/', form);             
          alert('Formulario enviado')
          this.$router.push('/');
        }

        const toggleDialog = () => {
            showMessage.value = !showMessage.value;
            if(!showMessage.value) {
                resetForm();
            }
        }
        const resetForm = () => {
            form.apellido_denunciante = '';
            form.categoria = null;
            form.descripcion = '';
            form.email_denunciante = '';
            form.latitud = '';
            form.longitud = '';
            form.nombre_denunciante = '';
            form.tel_cel_denunciante = null;
            form.titulo = '';
            submitted.value = false;
        }      
        return { form, v$, handleSubmit, toggleDialog, submitted, showMessage}
    },
    data(){
        return{
          url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
          attribution: '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
          zoom: 12,
          center: [lat, lng],
          markerLatLng: [lat, lng],                   
        }
      },  
    components: {
        LMap,
        LTileLayer,
        LMarker,
    },
    methods: {
        onReady (mapObject) {
        mapObject.locate();
        },
        onLocationFound(location){
        this.center = location.latlng
        },
        cancel(){
            this.$router.push("/");
        },
        get_point(e) {
          if (e.latlng) {
            this.markerLatLng = e.latlng;
            this.form.latitud = this.markerLatLng["lat"];
            this.form.longitud = this.markerLatLng["lng"];              
          }   
        }  
    }
}
</script>


<style scoped>
.container{
	height: 78vh;
}
.text-fields {
  background-color: green;
}

.text-fields-error {
  background-color: red;
}
.left{
    text-align: left;
}
label{
    font-weight:700;
}

.map-container{
    margin-bottom: 10px;
    margin-top: 10px;
}

@media(max-width: 576px){
    #mapid{
        height: 500px;
        width: 450px;
    }
}
  @media(min-width: 576px){
    #mapid{
        height: 500px;
        width: 600px;
    }
}

#lat, #lng{
    display:  none;        
}
body {
  /* background-image: url('images/loginImage.jpeg'); */
  font-family: 'Montserrat', Helvetica, sans-serif;
  font-size: 14px;
  background-repeat: no-repeat;
  background-size: cover;
  line-height: 18px;
  background-color: #F9F8F8;
}

.clear {
  clear: both;
  height: 0;
  overflow: hidden;
}

#container {
  width: 75%;
  margin: 0 auto;
  background-color: #FFF;
  padding: 20px 40px;
  border: solid 1px black;
  margin-top: 20px;
  min-height: 400px;
}

a.link {
  text-transform: uppercase;
  font-size: 10px;
  background-color: #92a4ad;
  padding: 10px 15px;
  border-radius: 0;
  color: #416475;
  display: inline-block;
  margin-right: 5px;
  margin-bottom: 5px;
  line-height: 1.5;
  text-decoration: none;
  margin-top: 50px;
  letter-spacing: 1px;
}

.contenido{
  min-height: calc(100vh - 70px - 90px);
}

.content-page{
  margin: 1rem;
}

.centered {
  padding-left: 30% !important;
}

.text-center{
  text-align: center;
}

.right{
text-align: right;
}

.left{
  text-align: left;
}

#submitButton{
  border: none !important;
  background: none !important;
}

.btn-primary {
  background-color: var(--primary-color) !important;
  border-color: var(--primary-color) !important;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.btn-primary:hover{
  background-color: var(--primary-color) !important;
  filter: brightness(95%);
}
.border-botton-dotted{
  border-bottom: 2px solid var(--primary-color) !important;;
  width: 30%;
  padding: 1rem;
}
.ml-1{
  margin-left: 1rem;
}
.ml-2{
  margin-left: 2rem;
}
.ml-3{
  margin-left: 3rem;
}
.ml-4{
  margin-left: 4rem;
}
.ml-5{
  margin-left: 5rem;
}
.mr-1{
  margin-right: 1rem;
}
.mr-2{
  margin-right: 2rem;
}
.mr-3 {
  margin-right: 3rem;
}
.mr-4 {
  margin-right: 4rem;
}
.mr-5 {
  margin-right: 5rem;
}
.mr-6 {
  margin-right: 6rem;
}
.mr-7 {
  margin-right: 7rem;
}
.mr-8 {
  margin-right: 8rem;
}
.mr-9 {
  margin-right: 9rem;
}
.mr-10 {
  margin-right: 10rem;
}
.mr-20 {
  margin-right: 20rem;
}
.mt-1{
  margin-top: 1rem;
}
.mt-2{
  margin-top: 2rem;
}
.mt-3{
  margin-top: 3rem;
}
.mt-4{
  margin-top: 4rem;
}
.mt-5{
  margin-top: 5rem;
}
.mb-1{
  margin-bottom: 1rem;
}
.mb-2{
  margin-bottom: 2rem;
}
.mb-3{
  margin-bottom: 3rem;
}
.mb-4{
  margin-bottom: 4rem;
}
.mb-5{
  margin-bottom: 5rem;
}
.pl-1 {
  padding-left: 1rem;
}
.pl-2 {
  padding-left: 2rem;
}
.pl-3 {
  padding-left: 3rem;
}
.pl-4 {
  padding-left: 4rem;
}
.pl-5 {
  padding-left: 5rem;
}
.pr-1{
  padding-right: 1rem;
}
.pr-2{
  padding-right: 2rem;
}
.pr-3{
  padding-right: 3rem;
}
.pr-4{
  padding-right: 4rem;
}
.pr-5{
  padding-right: 5rem;
}
.pt-1{
  padding-top: 1rem;
}
.pt-2{
  padding-top: 2rem;
}
.pt-3{
  padding-top: 3rem;
}
.pt-4{
  padding-top: 4rem;
}
.pt-5{
  padding-top: 5rem;
}
.pb-1{
  padding-bottom: 1rem;
}
.pb-2{
  padding-bottom: 2rem;
}
.pb-3{
  padding-bottom: 3rem;
}
.pb-4{
  padding-bottom: 4rem;
}
.pb-5{
  padding-bottom: 5rem;
}
.checkbox-1x {
  transform: scale(1.5);
  -webkit-transform: scale(1.5);
}
.checkbox-2x {
  transform: scale(2);
  -webkit-transform: scale(2);
}
</style>
