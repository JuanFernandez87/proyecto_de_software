<template>
  <div class="container">
    <h1 class="border-botton-dotted left">Zonas Inundables</h1>
    <div class="mt-5">
      <div class="form-row mb-2">
        <div class="input-group">
          <div class="form-group col-md-8 pr-2 left">
            <l-map
              class="map-container"
              @ready="onReady"
              @locationfound="onLocationFound"
              :zoom="zoom"
              :center="center"
            >
              <l-tile-layer
                :url="url"
                :attribution="attribution"
              ></l-tile-layer>
              <div v-for="(zona, index) in zonas" :key="zonas - { index }">
                <l-polygon
                  :lat-lngs="[zona.coordenadas]"
                  :color="zona.color"
                  :fill="true"
                  :fill-color="zona.color"
                  :fillOpacity="0.5"
                >
                  <l-popup>
                    <div>{{ zona.nombre }}</div>
                  </l-popup>
                </l-polygon>
              </div>
            </l-map>
          </div>
          <div class="form-group col-md-4 pl-1">
            <Card class="ml-2">
              <template #header> </template>
              <template #title class="title">
                Listado de zonas inundables:
              </template>
              <template #content>
                <div
                  v-for="(zona, index) in zonas"
                  :key="zonas - link - { index }"
                >
                  <router-link
                    :to="{ name: 'details', params: { zonaId: zona.id } }"
                    >{{ zona.nombre }}</router-link
                  >
                </div>
              </template>
            </Card>
          </div>
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
      zonas: [],
    };
  },
  created() {
    fetch(process.env.VUE_APP_API_URL + "zonas-inundables/all")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        console.log(json);
        this.zonas = json.zonas;
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

.left {
  text-align: left;
}
.border-botton-dotted {
  border-bottom: 2px solid var(--primary-color) !important;
  width: 30%;
  padding: 1rem;
}
.mt-5 {
  margin-top: 5rem;
}
.btn-primary {
  background-color: var(--primary-color) !important;
  border-color: var(--primary-color) !important;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.btn-primary:hover {
  background-color: var(--primary-color) !important;
  filter: brightness(95%);
}
.ml-2 {
  margin-left: 2rem;
}
</style>
