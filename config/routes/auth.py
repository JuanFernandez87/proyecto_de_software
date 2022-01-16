from app.resources import auth

def set_routes(app):
    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/login_Google", "auth_loginGoogle", auth.loginGoogle)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule("/register_Google", "auth_register_Google", auth.registerGoogle)
    app.add_url_rule("/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"])
    app.add_url_rule("/login/callback", "auth_callback", auth.callback, methods=["GET"])
    app.add_url_rule("/register/callback", "auth_callback_register", auth.callbackRegister, methods=["GET"])
