import { ZoneMape } from "./maps/MapZoneMarkerShow.js"

window.onload = () => {
  var id = $("#id").val();
  obtenerArea(id);
};

/** Obtiene el area de la recorrido y marca las coordenadas en el mapa */
function obtenerArea(id) {
  $.ajax({
    url: "/recorridos/ObtenerRecorridos/" + id,
    type: "GET",
    success: function (data) {
      const map = new ZoneMape({
        selector: "map",
        coordenadas: data,
      });
    },
    error: function (error) {
      console.log(error);
    },
  });
}
