import { ZoneMape } from  "./maps/MapZoneMarker.js"

const submitHander = (event , map) => {
    event.preventDefault();

    if (!map.hasValidZone()) {
        alert('Debes seleccionar un recorrido en el mapa');
    }
    else
    {
        const nombre = $('#nombre').val();
        const descripcion =$('#descripcion').val();
        const estado =$('#estado').val();
        const coordinates = map.drawnlayers[0].getLatLngs().flat().map(coordinate => {
            return { lat: coordinate.lat, lng: coordinate.lng}
        });
        const formData = new FormData();
        formData.append('nombre',nombre);
        formData.append('descripcion',descripcion);
        formData.append('estado',estado);
        formData.append('coordinates',JSON.stringify(coordinates));

        
        fetch('/recorridos/create', {
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
    const map = new ZoneMape({
        selector : 'map',
        addSearch : false,
    });


    const form = document.getElementById('create-recorrido-form');

    form.addEventListener('submit', (event) => submitHander(event, map));
    

};




