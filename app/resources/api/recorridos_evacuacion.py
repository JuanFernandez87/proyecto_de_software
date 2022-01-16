from flask import jsonify, Blueprint
from app.models.recorrido import Recorrido
from app.schemas.busqueda import Busqueda
from app.models.config_sistema import Config_sistema
import random


recorridos_evacuacion_api = Blueprint(
    "recorridos", __name__, url_prefix="/recorridos-evacuacion")


@recorridos_evacuacion_api.get("/<page>")
def per_page(page):
    try:
        page = int(page)
        config = Config_sistema.get_public_config()
        per_page = config.cant_elem
        order = config.orden

        recorrido = Busqueda.paginar_clase(
            Recorrido, page, per_page, order).items
        array_recorrido = Recorrido.obtener_json(recorrido)

        # Total de elementos en la página
        cant_recorrido = len(array_recorrido)
        return jsonify(recorrido=array_recorrido, total=cant_recorrido, pagina=page), 200
    except:
        return jsonify({'detalle': '500 Internal Server Error'}), 500


@recorridos_evacuacion_api.get("/")
def all():
    try:
        recorrido = Recorrido.all()
        array_recorrido = Recorrido.obtener_json(recorrido)
        return jsonify(recorrido=array_recorrido)
    except:
        return jsonify({'detalle': '500 Internal Server Error'}), 500
