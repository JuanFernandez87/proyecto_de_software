<template>
<div class="container">
  <h1 class="border-botton-dotted left">Mapa de denuncias en trámite</h1>
  
  <div class="mt-5">
    <div class="form-row mb-2">
       <div class="input-group">
        <div class="form-group col-md-8 pr-2 left" id="mapid">
          <l-map class="map-container" @ready="onReady" @locationfound="onLocationFound" :zoom="zoom" :center="center" >
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <div v-for="(denuncia, index) in denuncias" :key="denuncias - { index }">
              <div v-if="denuncia.estado != 'Sin confirmar'" >
                <l-marker  :lat-lng="[denuncia.latitud, denuncia.longitud]">
                    <l-popup>
                    <div> Estado: {{ denuncia.estado }} </div>
                    <div> Titulo: {{ denuncia.titulo }} </div>
                    <div> Descripcion: {{ denuncia.descripcion }} </div>                            
                    </l-popup>
                </l-marker>
                </div>  
            </div>
          </l-map>
          </div>

            <div class="form-group col-md-4 pl-1">
              <Card style="width: 25rem; margin-bottom: 2em" class="ml-4">
                  <template #title>
                      Informe denuncias
                  </template>
                  <template #content>
                      <p>En este mapa podrá encontrar información referida a las denuncias que se estan tramitando.</p>
                      <p>Para poder ver el estado e información presione sobre la marca en la ubicación de la denuncia.</p>
                  </template>
              </Card>
            </div>
       </div>
     </div>
  </div> 
</div>

</template>

<script>
import { LMap, LTileLayer, LMarker, LPopup } from "@vue-leaflet/vue-leaflet";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
  },
  methods: {
    onReady(mapObject) {
      mapObject.locate();
    },
    onLocationFound(location) {
      this.center = location.latlng;
    },
    mostrar: function (lat,long) {
        this.zoom = 15        
        this.center = [lat,long]
        console.log(lat,long);
      },
    volver: function () {
        this.zoom = 12        
        this.center = [-34.92149,-57.954597]
        
      }
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 12,
      center: [-34.92149, -57.954597],
      denuncias: [],
    };
  },
  created() {
    fetch(process.env.VUE_APP_API_URL + "denuncias/")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        console.log(json);
        this.denuncias = json.denuncias;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>

<style scoped>
.container {
  height: 75vh;
  margin-top: 1rem;
}

.map-container {
  height: 60vh !important;
}

ul{
text-align: left
}

.border-botton-dotted{
  border-bottom: 2px solid var(--primary-color) !important;;
  width: 50%;
  padding: 1rem;
}

.left{
  text-align: left;
}

.mt-5 {
  margin-top: 5rem;
}

.ml-4 {
  margin-left: 4rem;
}
</style>