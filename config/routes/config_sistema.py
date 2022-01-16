from app.resources import config 

def set_routes(app):
    # Rutas de Configuracion del sistema
    app.add_url_rule("/configuracion", "config_index", config.configuracion)
    app.add_url_rule("/configuracion", "config_update", config.update, methods=["POST"])  