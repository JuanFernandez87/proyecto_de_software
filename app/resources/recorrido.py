from flask import redirect, render_template, request, url_for, session,jsonify,abort
from app.models.coordenada import Coordenada
from wtforms import Form, StringField, validators,SelectField
from app.models.recorrido import Recorrido
from app.models.config_sistema import Config_sistema
from wtforms.fields.simple import BooleanField, HiddenField
from app.schemas.busqueda import Busqueda
from flask_login import login_required
from app.helpers.permissions_decorator import permission_required
import app.helpers.Permisos as Permisos


class RecorridoForm(Form):

    id = HiddenField('')
    nombre = StringField('Nombre de Recorrido', [validators.DataRequired("Nombre de recorrido requerido.")])
    descripcion = StringField('Descripcion', [validators.DataRequired("Descripcion Requerida.")])
    # No se puede usar checkbox ya que siempre retorna un estado activo
    #estado = SelectField('Publicado',choices=[ ('SI'), ('NO')])
    estado = SelectField(u'Publidado', choices=[('True', 'SI'), ('False', 'NO')])
    coordenadas = StringField('Coordenadas')

@login_required
@permission_required(Permisos.RECORRIDOS_INDEX)
def index(page: int = 1) -> render_template:
    """Función que muestra el listado de los recorridos, si hay valores cargados en la session procesa la busqueda

    Args:
        page (int, optional): [description]. Defaults to 1.

    Returns:
        render_template: index.html , los recorrido a cargar en ese html
    """

    config = Config_sistema.get_private_config()
    per_page = config.cant_elem
    orden = config.orden

    if ('valor' or 'estado') in session:
        recorridos = Busqueda.procesar_busqueda(Recorrido,page, per_page, orden, session['valor'], session['estado'])
        
    else:
        recorridos = Busqueda.paginar_clase(Recorrido, page, per_page, orden)

    return render_template("recorridos/index.html", recorridos=recorridos)

@login_required
@permission_required(Permisos.RECORRIDOS_NEW)
def new():
    form = RecorridoForm(request.form)

    return render_template("recorridos/new.html", form= form)

@login_required
@permission_required(Permisos.RECORRIDOS_NEW)
def create():
    form = RecorridoForm(**request.form)
    if request.method == 'POST' and form.validate():
        new_recorrido = Recorrido(**request.form)
        coordenadas = eval(request.form.get('coordinates'))
        for coordenada in coordenadas:
                latitud = coordenada["lat"]
                longitud = coordenada["lng"]
                new_coordenada = Coordenada(latitud=latitud, longitud=longitud)
                new_recorrido.recorrido.append(new_coordenada)
        new_recorrido.estado = True if request.form.get("estado") == 'True' else False
        Recorrido.new_recorrido(new_recorrido)
        return redirect(url_for('recorrido_index'))

    return render_template("recorridos/new.html", form=form)

@login_required
@permission_required(Permisos.RECORRIDOS_SHOW)
def show(id):
    recorrido = Recorrido.get_by_id(id)
    return render_template("recorridos/show.html", recorrido=recorrido)


@login_required
@permission_required(Permisos.DENUNCIA_DESTROY)
def delete():

    id = int(request.form.get('recorrido_to_delete'))

    Recorrido.delete(id)

    return redirect(url_for("recorrido_index"))

@login_required
@permission_required(Permisos.ZONAS_UPDATE)
def update_index(id):


    recorrido = Recorrido.get_by_id(id)

    form = RecorridoForm(obj=recorrido)

    return render_template("recorridos/update.html", form=form)

@login_required
@permission_required(Permisos.RECORRIDOS_UPDATE)
def update():

    form = RecorridoForm(request.form)
    if request.method == 'POST' and form.validate():

        recorrido_id = int(request.form.get('id'))

        Recorrido.update_recorrido(recorrido_id, request.form)

        return redirect(url_for("recorrido_index"))

    return render_template("recorridos/update.html", form=form)

def obtener_recorridos(id):
    recorrido = Recorrido.get_by_id(id)

    recorrido_coordenadas = []
    recorrido = recorrido.recorrido

    for coord in recorrido:
        lat = coord.latitud
        lng = coord.longitud
        punto = [lat, lng]
        recorrido_coordenadas.append(punto)

    return jsonify(recorrido_coordenadas)
    
@login_required
@permission_required(Permisos.RECORRIDOS_INDEX)
def busqueda() -> redirect:
    """Recibe los datos por post y lo guarda en la session del usuario

    Return : redirecciona al modulo (index) de recorridos
    """


    valor_busqueda = request.form.get('valor_busqueda')
    estado = request.form.get('tipo_estado')

    session["valor"] = valor_busqueda
    session["estado"] = estado

    return redirect(url_for("recorrido_index"))
