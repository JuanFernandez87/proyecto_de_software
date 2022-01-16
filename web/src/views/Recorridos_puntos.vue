<template>
<div>
<<<<<<< HEAD
  <h1 class="border-botton-dotted left">
    Recorridos de Evacuación y Puntos de encuentro
  </h1>
  <div class="mt-5">
    <div class="map-container">
      <div id="mapid">
        <l-map
          @ready="onReady"
          @locationfound="onLocationFound"
          :zoom="zoom"
          :center="center"
=======
   <a name='arriba'></a>
  <h1 class="border-botton-dotted left">
    Recorridos de Evacuación y Puntos de encuentro
  </h1>
  <div class="map-container">
    <div id="mapid">
      <l-map
        @ready="onReady"
        @locationfound="onLocationFound"
        :zoom="zoom"
        :center="center"
        
      >

        <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
        <div v-for="(punto, index) in puntos" :key="puntos - { index }">
          <l-marker  :lat-lng="[punto.lat, punto.long]">
            <l-tooltip>
              <div>Nombre : {{ punto.nombre }}</div>
              <div>Dirección : {{ punto.dirección }}</div>
              <div>Teléfono : {{ punto.telefono }}</div>
              <div>Email : {{ punto.email }}</div>
            </l-tooltip>
          </l-marker>
        </div>
        <div
          v-for="(recorrido, index) in recorridos"
          :key="recorridos - { index }"
>>>>>>> b23722e472012288681b7aee8ba9726838690283
        >
          <l-polyline
            :lat-lngs="[recorrido.coordenadas]"
            :color="recorrido.color"
            :weight="4"
          >
<<<<<<< HEAD
            <l-polyline
              :lat-lngs="[recorrido.coordenadas]"
              :color="recorrido.color"
              :weight="4"
            >
              <l-popup>
                <div>{{ recorrido.nombre }}</div>
              </l-popup>
            </l-polyline>
          </div>
        </l-map>
      </div>
    </div>
    <button id="volver" class="btn btn-primary mt-2" v-on:click="volver()">
      Volver al centro
    </button>
    <div class="container">
      <div class="row justify-content-right">
        <div class="col">
          <Card>
            <template #header>
              <!-- <img src="../assets/puntos.png" class="image" /> -->
            </template>
            <template #title class="title">
              <b> Recorridos de Evacuación </b>
            </template>
            <template #content>
              <ul>
                <b>Lista de recorridos :</b>
                <li
                  v-for="(recorrido, index) in recorridos"
                  :key="recorridos - { index }"
                >
                  <br />Recorrido :{{ index + 1 }} <br />Nombre :{{
                    recorrido.nombre
                  }}
                  <br />Descripción :{{ recorrido.descripcion }}
                  <br style="color: {{ recorrido.color }}" />Color :
                  {{ recorrido.color }}<br />
                  <br />
                  <br />
                  <button
                    class="btn btn-primary mt-2"
                    v-on:click="
                      mostrar(
                        recorrido.coordenadas[1].lat,
                        recorrido.coordenadas[1].lng
                      )
                    "
                  >
                    Ver recorrido
                  </button>
                </li>
              </ul>
            </template>
          </Card>
        </div>
        <div class="col">
          <Card>
            <template #header>
              <!-- Poner icono -->
            </template>
            <template #title> <b> Puntos de Encuentro </b> </template>
            <template #content>
              <ul>
                <b>Lista de puntos :</b>
                <li v-for="(punto, index) in puntos" :key="puntos - { index }">
                  <br />Punto :{{ index + 1 }} <br />Nombre :
                  {{ punto.nombre }} <br />Direccion :{{ punto.direccion }}
                  <br />Telefono : {{ punto.telefono }} <br />Correo :{{
                    punto.email
                  }}
                  <br />
                  <br /><button
                    class="btn btn-primary mt-2"
                    v-on:click="mostrar(punto.lat, punto.long)"
                  >
                    Ver punto
                  </button>
                </li>
              </ul>
            </template>
          </Card>
        </div>
      </div>
    </div>
  </div>
</div>
=======
            <l-popup>
              <div>{{ recorrido.nombre }}</div>
            </l-popup>
          </l-polyline>
        </div>
      </l-map>
    </div>
  </div>
  <a class="btn btn-secondary mt-2 mr-1" href='#arriba' id="volver" v-on:click="volver()">Volver al centro</a>
  <div class="container">
    <div class="row justify-content-right">
      <div class="col">
        <Card>
          <template #header>
            <!-- <img src="../assets/puntos.png" class="image" /> -->
          </template>
          <template #title class="title"> <b> Recorridos de Evacuación </b> </template>
          <template #content>
               <ul>
                 <b>Lista de recorridos :</b>
              <li
                v-for="(recorrido, index) in recorridos"
                :key="recorridos - { index }"
              >
                <br>Recorrido :{{ index + 1}}
                <br>Nombre :{{ recorrido.nombre }} 
                <br>Descripción :{{ recorrido.descripcion }}
                <br>Color : <button id='color' v-on:click="color(recorrido.color)">{{recorrido.color}}</button>
                <br><a class="btn btn-primary mt-2" href='#arriba' v-on:click="mostrar(recorrido.coordenadas[1].lat,recorrido.coordenadas[1].lng)">Ver recorrido</a>
              </li>
            </ul>
          </template>
        </Card>
      </div>
      <div class="col">
        <Card
        >
          <template #header>
            <!-- Poner icono -->
          </template>
          <template #title> <b> Puntos de Encuentro </b> </template>
         <template #content>
               <ul>
                 <b>Lista de puntos :</b>
              <li
                v-for="(punto, index) in puntos"
                :key="puntos - { index }"
              >
                <br>Punto :{{ index + 1}}
                <br>Nombre : {{ punto.nombre }} 
                <br>Direccion :{{ punto.direccion }}
                <br>Telefono : {{ punto.telefono }}
                <br>Correo :{{ punto.email }} <br>
                <br><a class="btn btn-primary mt-2" href='#arriba'  v-on:click="mostrar(punto.lat,punto.long)">Ver punto</a>

              </li>
            </ul>
          </template>
        </Card>
      </div>
    </div>
  </div>
  </div>
>>>>>>> b23722e472012288681b7aee8ba9726838690283
</template>

<script>
import {
  LMap,
  LTileLayer,
  LMarker,
  LPopup,LTooltip,
  LPolyline,
} from "@vue-leaflet/vue-leaflet";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,LTooltip,
    LPolyline,
  },
  methods: {
    onReady(mapObject) {
      mapObject.locate();
    },
    onLocationFound(location) {
      this.center = location.latlng;
    },
      color(color){
        document.getElementById("color").style.backgroundColor= color
      }

    ,
    mostrar: function (lat,long) {
        this.zoom = 15        
        this.center = [lat,long]
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
      zoom: 15,
      center: [-34.92149, -57.954597],
      puntos: [],
      recorridos: [],
    };
  },
  created() {
    fetch(process.env.VUE_APP_API_URL + "puntos-encuentro/")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        console.log(json);
        this.puntos = json.puntos;
      })
      .catch((e) => {
        console.log(e);
      });

    fetch(process.env.VUE_APP_API_URL + "recorridos-evacuacion/")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        console.log(json);
        this.recorridos = json.recorrido;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>
<style scoped>

#volver{
  justify-content: center
}
.map-container {
  display: flex;
  justify-content: center;
}

#mapid {
  height: 500px;
  width: 1200px;
}


ul{
text-align: left
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
.border-botton-dotted {
  border-bottom: 2px solid var(--primary-color) !important;
  width: 50%;
  padding: 1rem;
  margin-left: 2rem;
}
.mt-5 {
  margin-top: 5rem;
}
.container {
  height: 75vh;
  margin-top: 1rem;
}

.left {
  text-align: left;
}
<<<<<<< HEAD
=======




>>>>>>> b23722e472012288681b7aee8ba9726838690283
</style>
