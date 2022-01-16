import {Map} from '../../static/js/MapSingleMarker.js';
const submitHandler = (event, map) => {
    let lat;
    let lng;

    if (!map.marker){
        event.preventDefault();
        alert('Debe seleccionar una ubicación');
    }
    else {
        lat = map.marker.getLatLng().lat;
        lng = map.marker.getLatLng().lng;

        $('#lat').val(lat);
        $('#lng').val(lng);
    }
}

window.onload = () => {

    const map = new Map({
        selector: 'mapid',
        addSearch: true,
        lat: document.getElementById('lat').value,
        lng: document.getElementById('lng').value
    });
    const form = document.getElementById('update-denuncia-form');
    form.addEventListener('submit', (event) => submitHandler(event, map));
}