from app.resources import puntos_de_encuentro as punto
def set_routes(app):        
    # Rutas de Puntos de Encuentro
    app.add_url_rule("/puntos_de_encuentro", "punto_index", punto.index)
    app.add_url_rule("/puntos_de_encuentro/<int:page>", "punto_index", punto.index)
    app.add_url_rule("/puntos_de_encuentro/busqueda","punto_busqueda", punto.busqueda, methods=["POST"])
    app.add_url_rule("/puntos_de_encuentro", "punto_create", punto.create, methods=["POST"]) 
    app.add_url_rule("/puntos_de_encuentro/nuevo", "punto_new", punto.new)
    app.add_url_rule("/puntos_de_encuentro/update", "punto_update", punto.update, methods=["POST"])
    app.add_url_rule("/puntos_de_encuentro/delete", "punto_delete", punto.punto_delete, methods=["POST"])
    app.add_url_rule("/puntos_de_encuentro/update/<int:id>", "punto_update_index", punto.update_index)
    app.add_url_rule("/puntos_de_encuentro/show/<int:id>", "punto_show", punto.show)

    