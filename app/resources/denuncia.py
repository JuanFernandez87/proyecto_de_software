from flask import redirect, render_template, request, url_for, session, abort, flash
from app.models.denuncia import Denuncia 
from app.models.config_sistema import Config_sistema
from app.helpers.forms.denuncia import UpdateForm, RegistrationFormCreate, FormFiltro
from app.models.permission import Permission
from flask_login import login_required, current_user
from app.helpers.permissions_decorator import permission_required
import app.helpers.Permisos as Permisos
from flask_login import login_required

@login_required
def index(page:int=1, search_query=''):
    # Seteo los valores para que la primera vez, cuando no se ingreso busqueda me muestre todas las denuncias
    search_estado='Todos'
    search_titulo=''
    search_fecha_inicio=''
    search_fecha_fin=''
    # Si se ingresaron datos en el filtrado ingresa y setea los valores para la busqueda
    if search_query != '':
        list = search_query.split(",")
        search_estado=list[0]
        search_titulo=list[1]
        search_fecha_inicio=list[2]
        search_fecha_fin=list[3]
    config = Config_sistema.get_private_config()
    per_page = config.cant_elem
    order = config.orden   
    formQuery = FormFiltro(request.form) 
    # Si no se ingreso algun filtro muestra todas las denuncias
    if search_estado == 'Todos' and search_titulo == '' and search_fecha_inicio == '' and search_fecha_fin == '':
        denuncias = Denuncia.all_paginated(page, per_page, order)
    else:    
    # Si se ingreso un filtro muestra 
        denuncias = Denuncia.procesar_busqueda(page, per_page, order, search_titulo, search_estado, search_fecha_inicio, search_fecha_fin)             
    fechas = []
    return render_template("denuncia/index.html", denuncias=denuncias, query=formQuery)

@login_required
def search():
    formQuery = FormFiltro(request.form)
    query = []
    query = formQuery.estado.data + ',' + formQuery.titulo.data + ',' + formQuery.fecha_inicio.data + ',' + formQuery.fecha_fin.data
    return redirect(url_for("denuncia_index", page = 1, search_query=query))    

@login_required
@permission_required(Permisos.DENUNCIA_DESTROY)
def denuncia_delete():    
    id = int(request.form.get('denuncia_to_delete'))
    Denuncia.delete(id)
    return redirect(url_for("denuncia_index"))

@login_required
def update_index(id):
    denuncia = Denuncia.query.get(id)
    form = UpdateForm(obj=denuncia)
    return render_template("denuncia/update.html", form=form) 

@login_required
def update():
    form = UpdateForm(request.form) 
    if request.method == 'POST' and form.validate():
        denuncia_id = int(request.form.get('id'))
        Denuncia.update_denuncia(denuncia_id, request.form)
        return redirect(url_for("denuncia_index")) 
    return render_template("denuncia/update.html", form=form)     

@login_required
def new():

    # if not Permission.has_permissions(current_user.id,"usuario__new"): 
    #     abort(403)

    form = RegistrationFormCreate(request.form)
    return render_template("denuncia/new.html", form= form)

@login_required
def create():

    # if not Permission.has_permissions(current_user.id,"usuario__new"): 
    #     abort(403)

    form = RegistrationFormCreate(request.form)
    if request.method == 'POST' and form.validate():
        # Creo la nueva denuncia
        new_denuncia = Denuncia(**request.form)
        
        ''' Guardo el nuevo usuario '''
        id_usuario = current_user.id
        Denuncia.new_denuncia(new_denuncia, id_usuario)
        return redirect(url_for("denuncia_index"))
    
    return render_template('denuncia/new.html', form=form)    