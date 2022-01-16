from app.resources import recorrido as recorrido
def set_routes(app):        
    # Rutas de Recorridos de evacuación
    app.add_url_rule("/recorridos", "recorrido_index", recorrido.index)
    app.add_url_rule("/recorridos/<int:page>", "recorrido_index", recorrido.index)
    app.add_url_rule("/recorridos/create", "recorrido_create", recorrido.create, methods=["POST"])
    app.add_url_rule("/recorridos/nuevo", "recorrido_new", recorrido.new)
    app.add_url_rule("/recorridos/delete", "recorrido_delete", recorrido.delete, methods=["POST"])
    app.add_url_rule("/recorridos/update/<int:id>", "recorrido_update_index", recorrido.update_index)
    app.add_url_rule("/recorridos/update", "recorrido_update", recorrido.update, methods=["POST"])
    app.add_url_rule("/recorridos/show/<int:id>", "recorrido_show", recorrido.show)
    app.add_url_rule("/recorridos/ObtenerRecorridos/<int:id>", "obtener_recorridos", recorrido.obtener_recorridos)
    app.add_url_rule("/recorridos-de-evacuacion/busqueda","recorrido_busqueda", recorrido.busqueda, methods=["POST"])


    
