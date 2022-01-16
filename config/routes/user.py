from app.resources import user

def set_routes(app):
    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios/<int:page>", "user_index", user.index)
    app.add_url_rule("/usuarios/<int:page><string:search_query>", "user_index", user.index)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)
    app.add_url_rule("/usuario/delete", "user_delete", user.user_delete, methods=["POST"])
    app.add_url_rule("/usuarios/update/<int:id>", "user_update_index", user.update_index)
    app.add_url_rule("/usuarios/update", "user_update", user.update, methods=["POST"])
    app.add_url_rule("/usuarios/activate/<int:id>", "user_activate", user.activate)
    app.add_url_rule("/usuarios/search", "user_search", user.search, methods=["POST"])