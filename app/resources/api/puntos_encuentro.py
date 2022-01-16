from flask import jsonify, Blueprint
from app.models.puntos_de_encuentro import Puntos
from app.models.config_sistema import Config_sistema
from app.schemas.busqueda import Busqueda

puntos_encuentro_api = Blueprint(
    "puntos", __name__, url_prefix="/puntos-encuentro")


@puntos_encuentro_api.get("/<page>")
def per_page(page):
    try:
        page = int(page)
        config = Config_sistema.get_public_config()
        per_page = config.cant_elem
        order = config.orden

        puntos = Busqueda.paginar_clase(Puntos, page, per_page, order).items
        array_puntos = Puntos.obtener_json(puntos)

        #Total de elementos en la página
        cant_puntos = len(array_puntos)

        return jsonify(puntos=array_puntos, total=cant_puntos,pagina =page), 200
    except:
        return jsonify({'detalle' : '500 Internal Server Error'}), 500 
        
@puntos_encuentro_api.get("/")
def all():
    try:
        puntos = Puntos.all()
        array_puntos = Puntos.obtener_json(puntos)
        return jsonify(puntos=array_puntos)
    except:
        return jsonify({'detalle' : '500 Internal Server Error'}), 500 