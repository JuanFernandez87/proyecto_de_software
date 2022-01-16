const initialLat = -34.90248;
const initialLng = -57.93357;
const mapLayerUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";

export class ZoneMape {
  #drawItems;

  constructor({ selector, coordenadas }) {
    this.#drawItems = new L.FeatureGroup();

    this.#initializeMap(selector, coordenadas);


  }

  #initializeMap(selector, coordenadas) {
    this.map = L.map(selector).setView([initialLat, initialLng], 13);
    L.tileLayer(mapLayerUrl).addTo(this.map);

    this.map.addLayer(this.#drawItems);

    /** Agrego al mapa el recorrido con sus coordenadas. */
    var recorrido = L.polyline(coordenadas);
    recorrido.addTo(this.map);
    this.map.fitBounds(recorrido.getBounds());

    // this.map.addControl(this.createControls);
  }


}
