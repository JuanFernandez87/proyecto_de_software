from os import environ
import os

class Config(object):
    """Base configuration."""

    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASS = "1234"
    DB_NAME = "proyecto_software"
    SECRET_KEY = "secret"

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass

class ProductionConfig(Config):
    """Production configuration."""

    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "root")
    DB_PASS = environ.get("DB_PASS", "1234")
    DB_NAME = environ.get("DB_NAME", "proyecto_software")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
    )
    os.environ['GOOGLE_CLIENT_ID'] = "616814546424-vmcpnk4vblfjiram9p4074ge6u4v90op.apps.googleusercontent.com"
    os.environ['GOOGLE_CLIENT_SECRET'] =  "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"
    os.environ['GOOGLE_DISCOVERY_URL'] =  "https://accounts.google.com/.well-known/openid-configuration"
    os.environ['redirect_uri_login'] = "https://admin-grupo19.proyecto2021.linti.unlp.edu.ar/login/callback"
    os.environ['redirect_uri_register'] = "https://admin-grupo19.proyecto2021.linti.unlp.edu.ar/register/callback"
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

class DevelopmentConfig(Config):
    """Development configuration."""

    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "root")
    DB_PASS = environ.get("DB_PASS", "1234")
    DB_NAME = environ.get("DB_NAME", "proyecto_software")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
    )

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    os.environ['GOOGLE_CLIENT_ID'] = "616814546424-vmcpnk4vblfjiram9p4074ge6u4v90op.apps.googleusercontent.com"
    os.environ['GOOGLE_CLIENT_SECRET'] =  "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"
    os.environ['GOOGLE_DISCOVERY_URL'] =  "https://accounts.google.com/.well-known/openid-configuration"
    os.environ['redirect_uri_login'] = "https://admin-grupo19.proyecto2021.linti.unlp.edu.ar/login/callback"
    os.environ['redirect_uri_register'] = "https://admin-grupo19.proyecto2021.linti.unlp.edu.ar/register/callback"
    


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "MY_DB_USER")
    DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
    DB_NAME = environ.get("DB_NAME", "MY_DB_NAME")

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    os.environ['GOOGLE_CLIENT_ID'] = "616814546424-vmcpnk4vblfjiram9p4074ge6u4v90op.apps.googleusercontent.com"
    os.environ['GOOGLE_CLIENT_SECRET'] =  "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"
    os.environ['GOOGLE_DISCOVERY_URL'] =  "https://accounts.google.com/.well-known/openid-configuration"
    os.environ['redirect_uri_login'] = "https://admin-grupo19.proyecto2021.linti.unlp.edu.ar/login/callback"
    os.environ['redirect_uri_register'] = "https://admin-grupo19.proyecto2021.linti.unlp.edu.ar/register/callback"


config = dict(
    development=DevelopmentConfig, test=TestingConfig, production=ProductionConfig
)
