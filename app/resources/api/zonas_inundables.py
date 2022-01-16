from flask import jsonify, Blueprint
from app.models.zonas_inundables import Zonas_Inundables
from app.models.config_sistema import Config_sistema

zonas_inundables_api = Blueprint("zonas", __name__, url_prefix="/zonas-inundables")

@zonas_inundables_api.get("/all")
def index():

    try:
        # page = int(page)
        # config = Config_sistema.get_public_config()
        # per_page = config.cant_elem
        # order = config.orden
        # zonas = Zonas_Inundables.all_paginated(page,per_page,order).items
        zonas = Zonas_Inundables.all()
        array_zonas = []

        for zona in zonas:
            array_coordenadas = []
            for coord in zona.area:
                json_coord = {
                    "lat": coord.latitud,
                    "lng": coord.longitud
                }
                array_coordenadas.append(json_coord)
            json_zona = {
                "id": zona.id,
                "nombre": zona.name,
                "coordenadas": array_coordenadas,
                "color": zona.color_capa,
                "cantidad": zona.cant_puntos,
                "code": zona.code
            }
            array_zonas.append(json_zona)

        return jsonify(zonas=array_zonas, total=len(array_zonas)), 200
    
    except:    
        return jsonify({'detalle' : '500 Internal Server Error'}), 500 

@zonas_inundables_api.get("/<id>")
def zona(id):
    try:
        zona = Zonas_Inundables.get_by_id(id)
        if zona:
            json_zona = {}
            if(zona):
                array_coordenadas = []

                for coord in zona.area:
                    json_coord = {
                        "lat": coord.latitud,
                        "lng": coord.longitud
                    }
                    array_coordenadas.append(json_coord)
    
                json_zona = {
                    "id": zona.id,
                    "nombre": zona.name,
                    "coordenadas": array_coordenadas,
                    "color": zona.color_capa,
                    "cantidad": zona.cant_puntos,
                    "code": zona.code
                }

            return jsonify(atributos=json_zona), 200
        
        return jsonify({'detalle' : 'Zona no encontrada'}), 404 
    
    except:    
        return jsonify({'detalle' : '500 Internal Server Error'}), 500 
