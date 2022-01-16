from app.models.recorrido import Recorrido
from . import user, auth, home, config_sistema, puntos, denuncia, zonas_inundables,recorridos

def set_routes(app):
    home.set_routes(app)
    auth.set_routes(app)
    user.set_routes(app)
    puntos.set_routes(app)
    config_sistema.set_routes(app)
    denuncia.set_routes(app)
    zonas_inundables.set_routes(app)
    recorridos.set_routes(app)
    


