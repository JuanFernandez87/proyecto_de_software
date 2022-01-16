import { ZoneMape } from "../../static/js/MapZoneMarker.js";

window.onload = () => {
  var id = $("#id").val();
  obtenerArea(id);
};

/** Obtiene el area de la zona y marca las coordenadas en el mapa */
function obtenerArea(id) {
  $.ajax({
    url: "/Zonas/ObtenerCoordenadas/" + id,
    type: "GET",
    success: function (data) {
      var color_capa = $("#color_capa").val();
      const map = new ZoneMape({
        selector: "mapid",
        colorMap: color_capa,
        coordenadas: data,
      });
    },
    error: function (error) {
      console.log(error);
    },
  });
}
