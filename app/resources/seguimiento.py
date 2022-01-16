from flask import redirect, render_template, request, url_for, session, abort
from app.models.denuncia import Denuncia
from app.models.seguimiento import Seguimiento 
from app.helpers.forms.seguimiento import UpdateForm, SeguimientoForm
from app.models.permission import Permission
from flask_login import login_required, current_user
from app.helpers.permissions_decorator import permission_required
import app.helpers.Permisos as Permisos

@login_required
def revision_index(id):
    # Obtengo la información de la denuncia
    denuncia = Denuncia.get_by_id(id)
    # Obtengo los seguimientos de la denuncia
    seguimientos = Denuncia.all_seguimientos(id)
    form_denuncia = UpdateForm(obj=denuncia)    
    return render_template("denuncia/revision_index.html", form_denuncia=form_denuncia, id=id, seguimientos=seguimientos) 

@login_required
def update(id):
    form_denuncia = UpdateForm(request.form) 
    if request.method == 'POST' and form_denuncia.validate():
        denuncia_id = id
        Denuncia.update_denuncia(denuncia_id, request.form)
        form_seguimiento = SeguimientoForm()
        return render_template("denuncia/seguimiento_new.html", form_seguimiento=form_seguimiento, id=id) 
    return render_template("denuncia/seguimiento_new.html", form_denuncia=form_denuncia, id=id)    

@login_required
def new(id):
    form_seguimiento = SeguimientoForm(request.form)      
    if request.method == 'POST' and form_seguimiento.validate():
        # Creo un nuevo seguimiento
        new_seguimiento = Seguimiento(**request.form)
        # Guardo el nuevo seguimiento.
        user_name = current_user.user_name
        id_denuncia = id
        Seguimiento.new_seguimiento(new_seguimiento, user_name, id_denuncia)
        return redirect(url_for("denuncia_index"))    
    return render_template("denuncia/seguimiento_new.html", form_seguimiento=form_seguimiento) 