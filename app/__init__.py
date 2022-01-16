from os import environ
from flask import Flask, Blueprint
from flask_session import Session
from config.config import config
from app import db
from app.resources.api.zonas_inundables import zonas_inundables_api
from app.resources.api.denuncia import denuncia_api
from app.resources.api.recorridos_evacuacion import recorridos_evacuacion_api
from app.resources.api.puntos_encuentro import puntos_encuentro_api
from app.helpers import handler
from app.helpers import config as helper_configuracion
from config.routes import set_routes
from flask_login import LoginManager
from app.models.user import User
from flask_cors import CORS

def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    app.config["JSON_SORT_KEYS"] = False
    # Configure db
    db.init_app(app)

    # Configuración flask-login
    login_manager = LoginManager()
    login_manager.login_view = 'auth_login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # seteo de rutas
    set_routes(app)

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(get_color_header=helper_configuracion.get_color_header)
    app.jinja_env.globals.update(get_color_footer=helper_configuracion.get_color_footer)
    app.jinja_env.globals.update(get_color_boton=helper_configuracion.get_color_boton)
  
   # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(zonas_inundables_api)
    api.register_blueprint(denuncia_api)
    api.register_blueprint(recorridos_evacuacion_api)
    api.register_blueprint(puntos_encuentro_api)

    app.register_blueprint(api)


    # Handlers de error.
    #app.register_sucess_handler(201, handler.created)
    app.register_error_handler(400, handler.bad_request)
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(403, handler.not_permissions_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(500, handler.server_error)

    # Retornar la instancia de app configurada
    return app
