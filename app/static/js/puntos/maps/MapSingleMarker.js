//Constantes.
const initiallat = -34.9187;
const initiallng = -57.956;
const mapLayerUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
export function Map({ selector, addSearch, lat =''  , lng = ''}) {
  //Propiedades
  let marker;
  let map;

  initializeMap(selector);


  if (addSearch) {
    addSearchControl();
  };

  map.addEventListener("click", (e) => {
    addMarker(e.latlng);
  });

  //Creacion del mapa
  function initializeMap(selector) {
    map = L.map(selector).setView([initiallat, initiallng], 13);
    L.tileLayer(mapLayerUrl).addTo(map);
    // Si vienen lat o lng con datos , agrego el marcador
    if (lat || lng != ''){
      addMarker({lat,lng})
    }
  };

  //Comportamiento
  function addMarker({ lat,lng }) {
    if (marker) {
      marker.remove();
    };

    marker = L.marker([lat, lng]).addTo(map);
  }


  return {
    get marker() {
      return marker;
    },
    addMarker: addMarker,
  };
}
