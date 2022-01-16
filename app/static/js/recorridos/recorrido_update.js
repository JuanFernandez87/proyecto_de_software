import { ZoneMape } from "./maps/MapZoneUpdate.js"

const submitHander = (event , map) => {
  event.preventDefault();

  if (!map.hasValidZone()) {
      alert('Debes seleccionar un recorrido en el mapa');
  }
  else
  {
      const id = $('#id').val();
      const nombre = $('#nombre').val();
      const descripcion =$('#descripcion').val();
      const estado =$('#estado').val();
      const coordinates = map.drawnlayers[0].getLatLngs().flat().map(coordinate => {
          return { lat: coordinate.lat, lng: coordinate.lng}
      });
      const formData = new FormData();
      formData.append('id',id)
      formData.append('nombre',nombre);
      formData.append('descripcion',descripcion);
      formData.append('estado',estado);
      formData.append('coordinates',JSON.stringify(coordinates));

      
      fetch('/recorridos/update', {
          method: 'POST',
          body: formData
      })
      .then((response)=>{         
        if(response.redirected){
            window.location.href = response.url;
        }
    })           
      }
  }

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

      const form = document.getElementById('update-recorrido-form');
      form.addEventListener('submit', (event) => submitHander(event, map));
  
    },
    error: function (error) {
      console.log(error);
    },
  });
}