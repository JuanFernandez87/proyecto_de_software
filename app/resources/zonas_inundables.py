from flask import redirect, render_template, request, url_for, session, abort, jsonify
from wtforms import Form, StringField, validators, BooleanField
from wtforms.fields.simple import HiddenField
import os
import pandas as pd
from app.models.zonas_inundables import Zonas_Inundables
from app.models.coordenada import Coordenada
from app.models.config_sistema import Config_sistema
import uuid
from ast import literal_eval
from flask_login import login_required
from app.helpers.permissions_decorator import permission_required
import app.helpers.Permisos as Permisos

class ZonaInundableForm(Form):

    id = HiddenField('')
    name = StringField('Nombre', render_kw={'readonly': True})
    code = StringField('Código', [validators.DataRequired("Código requerido.")], render_kw={'readonly': True})
    active = BooleanField('Publicado')
    color_capa = StringField('Color de la Capa', [ validators.DataRequired("Color de capa requerido.")])
    cant_puntos = StringField('Cantidad de Puntos',render_kw={'readonly': True})


@login_required
@permission_required(Permisos.ZONAS_UPDATE)
def generar_codigo():
    """Función que genera un código UUID para la Zona Inundable.

    Returns:
        Código de 32 caracteres hexadecimal.
    """
    return uuid.uuid4().hex

@login_required
@permission_required(Permisos.ZONAS_NEW)
def parseCSV(filePath):
    """Función que procesa el archivo csv de Zonas Inundables y los guarda en la BD.

    Args:

        filePath ruta del archivo ingresado.
    """

    col_names = ['name', 'area']

    csvData = pd.read_csv(filePath, names=col_names, header=None)
    for i, row in csvData.iterrows():

        if(i > 0):
            nueva_zona = Zonas_Inundables(name = row['name'], code=generar_codigo())

            coordenadas = literal_eval(row['area'])
            
            # El area debe tener al menos 3 coordenadas.
            if(len(coordenadas)>= 3):
                for coord in coordenadas:
                    latitud = coord[0]
                    longitud = coord[1]
                    new_coordenada = Coordenada(latitud=latitud, longitud=longitud)
                    nueva_zona.area.append(new_coordenada)
                    nueva_zona.cant_puntos = nueva_zona.cant_puntos+1

            Zonas_Inundables.new_zone(nueva_zona)

@login_required
@permission_required(Permisos.ZONAS_INDEX)
def index(page=1, search_query = ''):
    """Función que muestra el listado de zonas inundables

    Args:
        page (int, optional): [description]. Defaults to 1.
        search_query (string, optional) [description]. Defaults to "".

    Returns:
        render_template: index.html , las zonas inundables a cargar en ese html
    """

    config = Config_sistema.get_private_config()
    per_page = config.cant_elem
    order = config.orden

   
    # Obtengo los valores de búsqueda nombre y estado si existen en el string de búsqueda.
    search_query_name = ""
    search_query_active = ""
    if(len(search_query) > 0):
        querys = search_query.split(",")
        search_query_name = querys[0]
        search_query_active = querys[1]

    if(not search_query):
        zonas = Zonas_Inundables.all_paginated(page, per_page, order)
    else:
        zonas = Zonas_Inundables.search(search_query, page, per_page, order)

    
    return render_template("zonas_inundables/index.html", zonas=zonas, search_value_name=search_query_name, search_value_active=search_query_active)

@login_required
@permission_required(Permisos.ZONAS_UPDATE)
def upload():
    """Función que carga el archivo csv de zonas inundables ingresado

    Returns:
        render_template: index.html , las zonas inundables que se cargaron con el archivo csv.
    """
    uploaded_file = request.files['file']
    ext = os.path.splitext(uploaded_file.filename)[1].strip(".")
    errors = ""

    if uploaded_file.filename != '' and ext == "csv":
        Zonas_Inundables.delete_all()
        file_path = os.path.join("app/static/uploads/", uploaded_file.filename)
        # set the file path
        uploaded_file.save(file_path)
        # save the file
        parseCSV(file_path)
    else:
        errors = "Debe seleccionar un archivo." if (
            uploaded_file.filename == '') else "La extensión del archivo deber ser csv."

    config = Config_sistema.get_private_config()
    per_page = config.cant_elem
    order = config.orden
    zonas = Zonas_Inundables.all_paginated(1, per_page, order)

    return render_template("zonas_inundables/index.html", zonas=zonas, errors=errors,  search_value_name = "", search_value_active="")

@login_required
@permission_required(Permisos.ZONAS_DESTROY)
def zone_delete():
    """Función borra una zona inundable.

    Returns:
        redirect to : index.html.
    """

    id = int(request.form.get('zone_to_delete'))

    Zonas_Inundables.delete(id)

    return redirect(url_for("zonas_index"))

@login_required
@permission_required(Permisos.ZONAS_INDEX)
def update_index(id):
    """Función que redirige a la pantalla de edicion de una zona inundable.
    Args:
        id (int): [description]

    Returns:
        render_template: update.html vista de edición de la zona inundable.
    """

    zona = Zonas_Inundables.get_by_id(id)

    form = ZonaInundableForm(obj=zona)

    return render_template("zonas_inundables/update.html", form=form)

@login_required
@permission_required(Permisos.ZONAS_UPDATE)
def update():
    """Función que edita una zona inundable

    Returns:
        redirect: index.html de zonas inundables
    """

    form = ZonaInundableForm(request.form)

    if request.method == 'POST' and form.validate():

        zona_id = int(request.form.get('id'))

        Zonas_Inundables.update_zona(zona_id, request.form)

        return redirect(url_for("zonas_index"))

    return render_template("zonas_inundables/update.html", form=form)

@login_required
@permission_required(Permisos.ZONAS_SHOW)
def detail(id):
    """Función que muestra la pantalla de detalle de una zona inundable.

    Args:
        id (int)

    Returns:
        render_template: detail.html , detalle de una zona inundable.
    """

    zona = Zonas_Inundables.get_by_id(id)

    return render_template("zonas_inundables/detail.html", zona=zona)

@login_required
@permission_required(Permisos.ZONAS_SHOW)
def obtener_coordenadas(id):
    """Función que obtiene las coordenadas de una zona inundable

    Args:
        id (int)

    Returns:
        JSON: con un array de las coordenadas del area de la zona inundable.
    """
    zona = Zonas_Inundables.get_by_id(id)

    area_coordenadas = []
    area = zona.area

    for coord in area:
        lat = coord.latitud
        lng = coord.longitud
        punto = [lat, lng]
        area_coordenadas.append(punto)

    return jsonify(area_coordenadas)

@login_required
@permission_required(Permisos.ZONAS_SHOW)
def search():

    """Función que busca por nombre de zona inundable y por estado.

    """

    name_query = request.form.get('name_query')
    active_query = request.form.get('active_query')

    search_query = name_query + ',' + active_query

    return redirect(url_for("zonas_index", page = 1, search_query = search_query))