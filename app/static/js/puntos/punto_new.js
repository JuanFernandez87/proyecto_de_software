import { Map } from  "./maps/MapSingleMarker.js"

const submitHander = (event , map) => {
    if (!map.marker) {
        event.preventDefault();
        alert('Debes seleccionar una ubicacion en el mapa');
    }
    else
    {
        document.getElementById('lat').setAttribute('value',map.marker.getLatLng().lat);
        document.getElementById('lng').setAttribute('value',map.marker.getLatLng().lng);
    }
}


    window.onload = () => {
    const map = new Map({
        selector : 'map',
        addSearch : false,
    });


    const form = document.getElementById('create-punto-form');

    form.addEventListener('submit', (event) => submitHander(event, map));
    

};




