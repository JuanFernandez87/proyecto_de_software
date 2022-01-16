from flask import redirect, render_template, request, url_for
from wtforms import Form, StringField, PasswordField, validators, ValidationError, BooleanField, SelectMultipleField
from wtforms.fields.simple import HiddenField
from wtforms.widgets import PasswordInput
from app.models.user import User
from app.models.rol import Rol
from app.models.config_sistema import Config_sistema
from flask_login import login_required
from app.helpers.permissions_decorator import permission_required
import app.helpers.Permisos as Permisos

roles = [('1', 'Administrador'), ('2', 'Operador')]

class UserForm(Form):
    
    def validate_user_name_unique(form, field):
        if User.exists_name(form.id.data, field.data) :
            raise ValidationError("El nombre de usuario ya existe.")
    def validate_email_unique(form, field):
        if User.exists_email(form.id.data, field.data) :
            raise ValidationError("El email ingresado ya existe.")

    id = HiddenField('')
    user_name = StringField('Nombre de Usuario', [validators.DataRequired("Nombre de usuario requerido."), validate_user_name_unique])
    email = StringField('Email', [validators.DataRequired("Email Requerido."), validate_email_unique, validators.Email("Formato de email inválido.")])
    first_name = StringField('Nombre', [validators.DataRequired("Nombre requerido.")])
    last_name = StringField('Apellido', [validators.DataRequired("Apellido requerido.")])
    password = PasswordField('Contraseña', [validators.DataRequired("Contraseña requerida.")], widget=PasswordInput(hide_value=False))
    active = BooleanField('Activo')
    rol_id = SelectMultipleField('Roles', [validators.DataRequired("Seleccionar al menos un rol.")], choices=roles)
    
@login_required
@permission_required(Permisos.USUARIO_INDEX)
def index(page = 1, search_query = ''):
    
    config = Config_sistema.get_private_config()
    per_page = config.cant_elem
    order = config.orden

    if(not search_query):
        users = User.all_paginated(page, per_page, order)
    else:
        users = User.search(search_query, page, per_page, order)

    return render_template("user/index.html", users=users, search_value = search_query)

@login_required
@permission_required(Permisos.USUARIO_NEW)
def new():

    form = UserForm(request.form)

    return render_template("user/new.html", form= form)

@login_required
@permission_required(Permisos.USUARIO_NEW)
def create():

    form = UserForm(request.form)
    
    if request.method == 'POST' and form.validate():
        # Obtengo los roles seleccionados. 
        roles_selected = Rol.get_by_ids(request.form.getlist("rol_id"))

        # Creo el nuevo usuario.
        new_user = User(**request.form)

        # Seteo si el usuario debe estar activo.
        new_user.active = True if request.form.get("active") else False
    
        # Guardo el nuevo usuario.
        new_user.roles.extend(roles_selected)
        
        User.new_user(new_user)

        return redirect(url_for("user_index"))
    
    return render_template('user/new.html', form=form)

@login_required
@permission_required(Permisos.USUARIO_DESTROY)
def user_delete():

    id = int(request.form.get('user_to_delete'))

    User.delete(id)

    return redirect(url_for("user_index"))

@login_required
@permission_required(Permisos.USUARIO_UPDATE)
def update_index(id):

    user = User.get_by_id(id)

    user.rol_id = [rol.id for rol in user.roles]

    form = UserForm(obj=user)

    return render_template("user/update.html", form=form) 

@login_required
@permission_required(Permisos.USUARIO_UPDATE)
def update():

    form = UserForm(request.form)

    if request.method == 'POST' and form.validate():
        
        # Obtengo los roles seleccionados. 
        roles_selected = Rol.get_by_ids(request.form.getlist("rol_id"))

        user_id = int(request.form.get('id'))

        User.update_user(user_id, request.form, roles_selected)
    
        return redirect(url_for("user_index"))  
    
    return render_template("user/update.html", form=form) 

@login_required
@permission_required(Permisos.USUARIO_UPDATE)
def activate(id):

    User.change_active(id)

    return redirect(url_for("user_index"))

@login_required
@permission_required(Permisos.USUARIO_SHOW)
def search():

    search = request.form.get('search_query')

    return redirect(url_for("user_index", page = 1, search_query = search))

