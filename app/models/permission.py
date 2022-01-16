from app.db import db
from sqlalchemy import Column, Integer, String

class Permission(db.Model):

    __tablename__ = "permission"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), unique=True)
    

    def __init__(self, name=None):
        self.name = name

    @staticmethod
    def get_permisos(user):
        #devuelve una lista con los nombres de los permisos de el usuario con el id recibido por parametro.
        permisos = []
        #obtenemos los roles del usuario.
        user_data = user
        #obtenemos los permisos asignados para los roles del usuario.
        roles = user_data.roles
        for per in roles:
            for var in per.permissions:
                if var not in permisos: # si hay permisos repetidos en los roles, en la lista solo aparecera una vez.
                    permisos.append(var)
        permisos = Permission.get_nombre_permisos(permisos)
        return permisos
        
    def get_nombre_permisos(lista_permisos):
        #recibe una lista con elem de tipo db permisos. 
        #devuelve una lista con los nombres de los permisos
        nombres_permisos = []
        for db_permiso in lista_permisos:
            id = db_permiso.id
            nombres_permisos.append(Permission.query.filter_by(id = id).first().name)
        return nombres_permisos
    
    @staticmethod
    def has_permissions(user, perm):
        if perm in Permission.get_permisos(user):
            return True
        return False