<template>
  <div class="container">
    <h1 class="border-botton-dotted left">Zona {{ zona.nombre }}</h1>
    <div class="mt-5">
      <div class="input-group">
        <div class="form-group col-md-8 pr-2 left">
          <l-map
            class="map-container"
            @ready="onReady"
            @locationfound="onLocationFound"
            :zoom="zoom"
            :center="center"
          >
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>

            <l-polygon
              :lat-lngs="[zona.coordenadas]"
              :color="zona.color"
              :fill="true"
              :fill-color="zona.color"
              :fillOpacity="0.5"
            >
              <l-popup>
                <div>Nombre: {{ zona.nombre }}</div>
                <div>Código: {{ zona.code }}</div>
                <div>Cantidad de Puntos: {{ zona.cantidad }}</div>
              </l-popup>
            </l-polygon>
          </l-map>
        </div>
        <div class="form-group col-md-2">
          <button class="btn btn-primary" @click="$router.go(-1)">
            Volver
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { LMap, LTileLayer, LPolygon, LPopup } from "@vue-leaflet/vue-leaflet";
export default {
  components: {
    LMap,
    LTileLayer,
    LPolygon,
    LPopup,
  },
  props: {
    zonaId: String,
  },
  methods: {
    onReady(mapObject) {
      mapObject.locate();
    },
    onLocationFound(location) {
      this.center = location.latlng;
    },
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 12,
      center: [-34.92149, -57.954597],
      zona: {
        coordenadas: [],
        color: "",
        nombre: "",
        cantidad: "",
        code: "",
      },
    };
  },

  created() {
    fetch(process.env.VUE_APP_API_URL + "zonas-inundables/" + this.zonaId)
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.zona = json.atributos;
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
.border-botton-dotted {
  border-bottom: 2px solid var(--primary-color) !important;
  width: 30%;
  padding: 1rem;
}
.mt-5 {
  margin-top: 5rem;
}

.left {
  text-align: left;
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
</style>
