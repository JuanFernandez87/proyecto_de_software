from app.resources import zonas_inundables

def set_routes(app):
    # Rutas de Zonas Inundables
    app.add_url_rule("/Zonas", "zonas_index", zonas_inundables.index)
    app.add_url_rule("/Zonas/<int:page>", "zonas_index", zonas_inundables.index)
    app.add_url_rule("/Zonas/<int:page><string:search_query>", "zonas_index", zonas_inundables.index)
    app.add_url_rule("/Zonas/Upload", "zonas_upload", zonas_inundables.upload, methods=["POST"])
    app.add_url_rule("/Zonas/Delete", "zone_delete", zonas_inundables.zone_delete, methods=["POST"])
    app.add_url_rule("/Zonas/Update/<int:id>", "zona_update_index", zonas_inundables.update_index)
    app.add_url_rule("/Zonas/Update", "zona_update", zonas_inundables.update, methods=["POST"])
    app.add_url_rule("/Zonas/GenerarCodigo", "generar_codigo", zonas_inundables.generar_codigo)
    app.add_url_rule("/Zonas/Detail/<int:id>", "zonas_detail", zonas_inundables.detail)
    app.add_url_rule("/Zonas/ObtenerCoordenadas/<int:id>", "obtener_coordenadas", zonas_inundables.obtener_coordenadas)
    app.add_url_rule("/Zonas/search", "zonas_search", zonas_inundables.search, methods=["POST"])