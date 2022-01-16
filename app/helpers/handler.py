from flask import render_template, request, jsonify

def created(e):
    kwargs = {
        "error_name": "201 Created",
        
        "error_description": "Se creo correctamente",
    }
    if request.path.startswith("/api/"):
        return jsonify(kwargs)
    else:      
        return render_template("error.html", error=kwargs), 201

def bad_request(e):
    kwargs = {
        "error_name": "400 Bad Request",
        
        "error_description": "Error del cliente",
    }
    if request.path.startswith("/api/"):
        return jsonify(kwargs)
    else:      
        return render_template("error.html", error=kwargs), 400

def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que quiere acceder no existe",
    }
    return render_template("error.html", error=kwargs), 404

def not_permissions_error(e):
    kwargs = {
        "error_name": "403 Forbidden",
        "error_description": "No posee permiso para acceder a la url",
    }
    return render_template("error.html", error=kwargs), 403

def unauthorized_error(e):
    kwargs = {
        "error_name": "401 Unauthorized Error",
        "error_description": "No está autorizado para acceder a la url",
    }
    return render_template("error.html", error=kwargs), 401

def server_error(e):
    kwargs = {
        "error_name": "500 Server Error",
        "error_description": "Error interno del servidor",
    }
    return render_template("error.html", error=kwargs), 500
