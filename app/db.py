from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"autoflush": False})

def init_app(app):
    db.init_app(app)
    with app.app_context():
        from app.models.rol import Rol
        from app.models.user import User
        from app.models.permission import Permission
        from app.models.config_sistema import Config_sistema
        from app.models.puntos_de_encuentro import Puntos
        from app.models.denuncia import Denuncia
        from app.models.zonas_inundables import Zonas_Inundables
        from app.models.coordenada import Coordenada
        from app.models.seguimiento import Seguimiento
        from app.models.recorrido import Recorrido
        from app.models.categoria import Categoria
    config_db(app)


def config_db(app):
    @app.before_first_request
    def init_database():
        db.create_all()

    @app.teardown_request
    def close_session(exception=None):
        db.session.remove()
