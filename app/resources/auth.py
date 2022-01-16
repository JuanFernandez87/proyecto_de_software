from flask import redirect, render_template, request, url_for, session
from app.models.user import User
from app.models.config_sistema import Config_sistema
from flask_login import login_user, logout_user, login_required
import requests
from oauthlib.oauth2 import WebApplicationClient
import json
from os import environ as env

#Configuracion credenciales Google
GOOGLE_CLIENT_ID = env['GOOGLE_CLIENT_ID']
GOOGLE_CLIENT_SECRET = env['GOOGLE_CLIENT_SECRET']
GOOGLE_DISCOVERY_URL = env['GOOGLE_DISCOVERY_URL']

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

client = WebApplicationClient(GOOGLE_CLIENT_ID)

def loginGoogle():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri= env['redirect_uri_login'],
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

def registerGoogle():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=env['redirect_uri_register'],
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        users_last_name = userinfo_response.json()["family_name"]
    else:
        return "User email not available or not verified by Google.", 400
        
    # Create a user in your db with the information provided
    # by Google
    # user_to_create = User(
    #     first_name=users_name, last_name=users_last_name, email=users_email, user_name=users_email
    # )

    # user = User.get(users_email)

    # if not user:
    #     User.new_user(user_to_create)
    #     return render_template("auth/login.html", success="Usuario creado con éxito.")

    user = User.get(users_email)

    if not user:
        return render_template("auth/login.html", errors="Usuario no registrado.")
    if not user.active:
        return render_template("auth/login.html", errors="El usuario no esta activado, por favor contacte con su administrador.")

    config = Config_sistema.get_private_config()
    
    color_header = config.color_header
    color_footer = config.color_footer
    color_button = config.color_button
    
    session["color_header"] = color_header
    session["color_footer"] = color_footer
    session["color_boton"] = color_button

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=True)

    # Send user back to homepage
    return redirect(url_for("home"))

def callbackRegister():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        users_last_name = userinfo_response.json()["family_name"]
    else:
        return "User email not available or not verified by Google.", 400
        
    # Create a user in your db with the information provided
    # by Google
    user_to_create = User(
        first_name=users_name, last_name=users_last_name, email=users_email, user_name=users_email
    )

    user = User.get(users_email)

    if not user:
        User.new_user(user_to_create)
        return render_template("auth/login.html", success="Usuario creado con éxito.")
    else :
        return render_template("auth/login.html", errors="El usuario ya se encuentra registrado.")

    # user = User.get(users_email)
    # if not user.active:
    #     return render_template("auth/login.html", errors="El usuario no esta activado, por favor contacte con su administrador.")

    # config = Config_sistema.get_private_config()
    
    # color_header = config.color_header
    # color_footer = config.color_footer
    # color_button = config.color_button
    
    # session["color_header"] = color_header
    # session["color_footer"] = color_footer
    # session["color_boton"] = color_button

    # # if the above check passes, then we know the user has the right credentials
    # login_user(user, remember=True)

    # Send user back to homepage
    # return redirect(url_for("home"))

def login():
    return render_template("auth/login.html")

def authenticate():
    params = request.form
    user = User.user_exists(params["email"], params["password"])

    if not user:
        return render_template("auth/login.html", errors="Email o contraseña incorrecta.")
    if not user.active:
        return render_template("auth/login.html", errors="El usuario no esta activado, por favor contacte con su administrador.")

    config = Config_sistema.get_private_config()
    
    color_header = config.color_header
    color_footer = config.color_footer
    color_button = config.color_button
    
    session["color_header"] = color_header
    session["color_footer"] = color_footer
    session["color_boton"] = color_button

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=True)
    return redirect(url_for("home"))

@login_required
def logout():
    for key in list(session.keys()):
     if not (key == "color_header" or key == "color_footer" or key == "color_boton"):
        session.pop(key)

    logout_user()
    return redirect(url_for("auth_login"))
