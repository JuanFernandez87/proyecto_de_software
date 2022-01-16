from app.resources import denuncia, seguimiento 

def set_routes(app):        
    # Rutas de Denuncia
    app.add_url_rule("/denuncia", "denuncia_index", denuncia.index)
    app.add_url_rule("/denuncia/<int:page>", "denuncia_index", denuncia.index)

    # Ruta para buscar 
    app.add_url_rule("/denuncia/search","denuncia_search", denuncia.search, methods=["POST"])

    # Ruta con filtrado
    app.add_url_rule("/denuncia/<int:page><string:search_query>", "denuncia_index", denuncia.index)    
    
    # Ruta para crear
    app.add_url_rule("/denuncia/nuevo", "denuncia_new", denuncia.new) 
    app.add_url_rule("/denuncia", "denuncia_create", denuncia.create, methods=["POST"]) 

    # Ruta para editar 
    app.add_url_rule("/denuncia/update/<int:id>", "denuncia_update_index", denuncia.update_index)
    app.add_url_rule("/denuncia/update", "denuncia_update", denuncia.update, methods=["POST"])

    # Ruta para eliminar
    app.add_url_rule("/denuncia/delete", "denuncia_delete", denuncia.denuncia_delete, methods=["POST"])

    # Ruta para revisar 
    app.add_url_rule("/denuncia/revision_index/<int:id>", "denuncia_revision_index", seguimiento.revision_index)
    app.add_url_rule("/denuncia/revision/<int:id>", "denuncia_revision", seguimiento.update, methods=["POST"]) 
    app.add_url_rule("/denuncia/seguimiento/<int:id>", "denuncia_revision_new", seguimiento.new, methods=["POST"]) 
    