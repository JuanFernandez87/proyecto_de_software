from flask import redirect, render_template, request, url_for, session, abort
from wtforms.widgets.core import CheckboxInput
from app.models.puntos_de_encuentro import Puntos
from app.models.config_sistema import Config_sistema
from app.models.permission import Permission
from wtforms import Form, StringField, validators, ValidationError,SelectField,IntegerField
from wtforms.fields.simple import BooleanField, HiddenField
from app.models.coordenada import Coordenada
from app.schemas.busqueda import Busqueda
from flask_login import login_required
from app.helpers.permissions_decorator import permission_required
import app.helpers.Permisos as Permisos
import ipdb

class RegistrationForm(Form):

    def validar_nombre_punto_unico(form, field):
        if Puntos.validar_nombre(form.id.data, field.data):
            raise ValidationError("El nombre de usuario ya existe.")

    def validar_coordenada_unica(form,field):
        if Puntos.validar_latitud(form.id.data, field.data) and Puntos.validar_longitud(form.id.data, field.data):
            raise ValidationError("La coordenada ingresada ya existe.")
    def length(min=5, max=40):
        message = 'Debe tener entre %d y %d caracteres' % (min, max)

        def _length(form, field):
            l = field.data and len(field.data) or 0
            if l < min or max != -1 and l > max:
                raise ValidationError(message)

        return _length
    
       
    id = HiddenField('')
    nombre = StringField('Nombre del Punto', [validators.DataRequired("Nombre de punto requerido."), length(max=25), validar_nombre_punto_unico])
    direccion = StringField('Dirección', [validators.DataRequired("Dirección requerida."), length()])
    estado = BooleanField('Publicado')
    telefono = IntegerField('Telefono', [validators.DataRequired("Telefono requerido.")]) #Falta validar length 
    email = StringField('Email', [validators.DataRequired("Email requerido."), validators.Email("Formato de email inválido.")])
    lat = StringField('Latitud')
    lng = StringField('Longitud')


@login_required
@permission_required(Permisos.PUNTO_INDEX)
def index(page: int = 1) -> render_template:
    """Función que muestra el listado de los puntos de encuentro, si hay valores cargados en la session procesa la busqueda

    Args:
        page (int, optional): [description]. Defaults to 1.

    Returns:
        render_template: index.html , los puntos a cargar en ese html
    """

    config = Config_sistema.get_private_config()
    per_page = config.cant_elem
    orden = config.orden
    
    if ('valor' or 'estado') in session:
        puntos = Busqueda.procesar_busqueda(Puntos,page, per_page, orden, session["valor"], session["estado"])


    else:
        puntos = Busqueda.paginar_clase(Puntos, page, per_page, orden)

    return render_template("puntos/index.html", puntos=puntos)

@login_required
@permission_required(Permisos.PUNTO_SHOW)
def show(id):

    coordenadas = Puntos.obtener_coordenadas_por_id_de_punto(id)
    
    return render_template("puntos/show.html", coordenadas=coordenadas)

@login_required
@permission_required(Permisos.PUNTO_INDEX)
def busqueda() -> redirect:
    """Recibe los datos por post y lo guarda en la session del usuario

    Return : redirecciona al modulo de puto de encuentro 
    """


    valor_busqueda = request.form.get('valor_busqueda')
    estado = request.form.get('tipo_estado')

    session["valor"] = valor_busqueda
    session["estado"] = estado
    # Guardarlo en la session me sirve para utilizar lo también en puntos de encuentro(P.E)
    # Ej: si busco por Despublicados en Recorridos y voy a P.E me muestran los P.E despublicados
    return redirect(url_for("punto_index"))

@login_required
@permission_required(Permisos.PUNTO_NEW)
def new():
    """Carga la vista para ingresar un punto de encuentro

    Returns:
        render_template: [description]
    """


    p = request.form

    form = RegistrationForm(p)

    return render_template("puntos/new.html", form=form)

@login_required
@permission_required(Permisos.PUNTO_NEW)
def create():
    form = RegistrationForm(request.form)
 
    if request.method == 'POST' and form.validate():
        coordenadas = Coordenada(request.form.get('lat'),request.form.get('lng'))
        new_punto = Puntos(**request.form)
        #Si el estado es publicado , nos retorna 'y', y si no no retorna nada por lo tanto
        new_punto.estado = True if request.form.get("estado") else False
        coordenadas.punto.append(new_punto)
        Coordenada.new_coordenada(coordenadas)
        Puntos.new_punto(new_punto)
        return redirect(url_for("punto_index"))

    return render_template("puntos/new.html", form=form)

@login_required
@permission_required(Permisos.PUNTO_UPDATE)
def update():

    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():

        punto_id = int(request.form.get('id'))
        id_coordenada = Puntos.obtener_punto_por_id(punto_id).id_coordenada

        Coordenada.update_coordenada(id_coordenada,request.form)
        Puntos.update_punto(punto_id, request.form)
        return redirect(url_for("punto_index"))

    return render_template("puntos/update.html", form=form)

@login_required
@permission_required(Permisos.PUNTO_DESTROY)
def punto_delete() -> redirect:
    """Controlador para borrar un punto mediante una id

    Returns:
        redirect: [ vuelve a el index sea borrado o no el punto de encuetro]
    """


    id = int(request.form.get('punto_to_delete'))

    id_coordenada = Puntos.obtener_punto_por_id(id).id_coordenada

    Coordenada.delete(id_coordenada)    
    Puntos.delete(id)


    return redirect(url_for("punto_index"))

@login_required
@permission_required(Permisos.PUNTO_UPDATE)
def update_index(id):
    punto = Puntos.obtener_punto_por_id(id)
    coordenadas = Puntos.obtener_coordenadas_por_id_de_punto(id)
    form = RegistrationForm(obj=punto)
    form.lat.data = coordenadas["lat"]
    form.lng.data = coordenadas["lng"]

    return render_template("puntos/update.html", form=form)
