import { Map } from  "./maps/MapSingleMarker.js"


const submitHander = (event , map) => {
    if (!map.marker) {
        event.preventDefault();
        alert('Debes seleccionar una ubicacion en el mapa');
    }
    else
    {
        document.getElementById('lat').setAttribute('value',map.marker.getLatLng().lat);
        document.getElementById('lng').setAttribute('value',map.marker.getLatLng().lng)

    }
}


    window.onload = () => {
    let lat = $("#lat").val();
    let lng = $("#lng").val();
    const map = new Map({
        selector : 'map',
        addSearch : false,
        lat,
        lng
    });


    const form = document.getElementById('update-punto-form');

    form.addEventListener('submit', (event) => submitHander(event, map));
    

};




