from flask import render_template

def set_routes(app):
    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("home.html")