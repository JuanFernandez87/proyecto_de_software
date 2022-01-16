from flask import app, redirect, render_template, request, url_for, session, Flask
from app.models.config_sistema import Config_sistema
from app.db import db
from flask_login import login_required

paletaHeader = {'Gris claro': '#B2B1B9', 
            'Blanco': '#FFFFFF',
            'Beige': '#D9CAB3'}

paletaFooter = {'Gris oscuro': '#212121', 
            'Negro': '#000000',
            'Marron oscuro': '#2D2424'}

paletaBotones = {'Naranja claro': '#FFA400', 
            'Verde claro': '#6D9886',
            'Verde': '#008290'}

cantidad = [5, 10, 15, 20]            

@login_required
def configuracion():
     # Cuando se implemente lo de sesion, esto no iria    
     publica = Config_sistema.query.filter_by(id=1).first()
     privada = Config_sistema.query.filter_by(id=2).first()
     #
     return render_template("mainConfig/config.html", coloresHeader=paletaHeader, coloresFooter=paletaFooter, coloresBotones=paletaBotones, publica=publica, privada=privada, cantidad=cantidad)

@login_required
def update():    

     publica, privada = db.session.query(Config_sistema).all()
     def armar_config(publica=True):
         value = "Publica" if publica else "Privada"
         return {"id": 1 if publica else 2,
         "orden": False if request.form.get('orden') == "0" else True,
         "cant_elem": request.form.get('cant'),
         "color_header": request.form.get('header{}'.format(value)),         
         "color_footer": request.form.get('footer{}'.format(value)),
         "color_button": request.form.get('botones{}'.format(value))}
         
     publica = Config_sistema.update(**armar_config())
     privada = Config_sistema.update(**armar_config(False))  

     session["color_header"] = request.form.get('header{}'.format("Privada"))
     session["color_footer"] = request.form.get('footer{}'.format("Privada"))
     session["color_boton"] = request.form.get('botones{}'.format("Privada"))

     if publica and privada:
         return redirect(url_for("config_index")) 
     return redirect(url_for("config_index")) 