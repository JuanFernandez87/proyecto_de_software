from flask import jsonify, Blueprint, request, abort, Response
from app.models.denuncia import Denuncia
from app.models.categoria import Categoria
from app.db import db
from app.helpers.forms.denuncia import RegistrationFormCreate

denuncia_api = Blueprint("denuncias", __name__, url_prefix="/denuncias")

@denuncia_api.get("/")
def index():
    denuncias_rows = Denuncia.query.all()
    denuncias = [denuncia.as_dict() for denuncia in denuncias_rows]
    return jsonify(denuncias=denuncias)

@denuncia_api.post("/")
def create():  
    '''' Función que recibe un formulario desde una app publica, verifica los campos y 
    si corresponde la almacena en la BD
    '''
    try:
        form = RegistrationFormCreate(**request.get_json())
        if form.validate():
            new_denuncia = Denuncia(**request.get_json())    
            # verifico que el ID de la categoría exista en la BD
            if Categoria.get_by_id(new_denuncia.categoria):
                # Creo la nueva denuncia y la almaceno
                Denuncia.new_denuncia_from_api(new_denuncia)
                return jsonify(new_denuncia.as_dict()),201
            return jsonify({'detalle' : 'La categoria ingresada no existe en el sistema'}), 409
        return jsonify({'detalle' : form.errors}), 400 
    except:    
        return jsonify({'detalle' : ''}), 500 