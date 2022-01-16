from sqlalchemy.sql.elements import and_
from app.db import db
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from flask_login import UserMixin, current_user
from app.models.permission import Permission


#one-to-many association table: users - roles
users_roles = Table('usuario_rol', db.metadata,
    Column('id_usuario', Integer, ForeignKey('users.id', ondelete='CASCADE')),
    Column('id_rol', Integer, ForeignKey('roles.id', ondelete='CASCADE')),
    PrimaryKeyConstraint('id_usuario', 'id_rol')
)

#one-to-many association table: users - denuncias
users_denuncias = Table('usuario_denuncia', db.metadata,
    Column('id_usuario', Integer, ForeignKey('users.id', ondelete='CASCADE')),
    Column('id_denuncia', Integer, ForeignKey('denuncias.id', ondelete='CASCADE')),
    PrimaryKeyConstraint('id_usuario', 'id_denuncia')
)
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True , autoincrement=True)
    first_name = Column(String(30)) 
    last_name = Column(String(30))
    email = Column(String(30), unique=True)
    password = Column(String(30))
    user_name = Column(String(30), unique=True)
    active = Column(Boolean)
    roles = relationship(
        'Rol',
        secondary=users_roles,
        backref='user_rol')
    denuncias = relationship(
        'Denuncia',
        secondary=users_denuncias,
        backref='user_denuncia')
        

    def __init__(self, first_name=None, last_name=None, email=None, password=None, user_name=None, active=False, rol_id=None, denuncia_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.user_name = user_name
        self.active = active
        self.rol_id = rol_id
        self.denuncia_id = denuncia_id

    def save(self):
        if not self.id:
            db.session.add(self)
            db.session.commit()

    def remove(self):
        if self.id != current_user.id:
            db.session.delete(self)
            db.session.commit()
    
    def update(self, values, roles):
        self.first_name = values.get('first_name')
        self.last_name = values.get('last_name')
        self.email = values.get('email')
        self.password = values.get('password')
        self.user_name = values.get('user_name')
        self.active = True if values.get('active') else False
        self.roles = roles

        db.session.commit()

    def update_active(self):
        self.active = not self.active
        db.session.commit()

    def has_role(self, rol):
        return rol in [i.name for i in self.roles]

    def has_permissions(user, perm):
        if perm in Permission.get_permisos(user):
            return True
        return False

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def all():
        return User.query.filter()

    @staticmethod
    def all_paginated(page, per_page, order):
        current_user_id = current_user.id
        sort_order = User.user_name.desc() if order else User.user_name.asc()
        return User.query.filter(User.id != current_user_id).order_by(sort_order).paginate(page, per_page, error_out=False)
    
    @staticmethod
    def delete(id):
        user = User.query.get(id)
        if user:
            user.remove()
            return True
        return False
    
    @staticmethod
    def new_user(user):
        if user:
            user.save()

    @staticmethod
    def update_user(id, values, roles):

        user_update = User.query.get(id)

        if user_update:
            user_update.update(values, roles)

    @staticmethod
    def change_active(id):
        user = User.get_by_id(id)
        if user:
         user.update_active()

    @staticmethod
    def search(query, page, per_page, order):
        look_for = '%{0}%'.format(query)
        sort_order = User.user_name.desc() if order else User.user_name.asc()
        response_query =  User.query.filter(User.user_name.like(look_for)).order_by(sort_order)
        return response_query.paginate(page=page, per_page=per_page)

    @staticmethod
    def user_exists(email, password):
        return User.query.filter( and_(User.email == email, User.password == password)).first()


    @staticmethod
    def exists_name(user_id, name):
        user_found = User.query.filter(User.user_name == name).first()
        user_name_exists = False
        if (user_found):
            user_name_exists = True
            # Si estoy editando un usuario tengo un user_id, si ese user_id es igual al encontrado, no valido el nombre de usuario duplicado.
            if(user_id):
                if(int(user_id) == int(user_found.id)):
                   user_name_exists = False        
        return user_name_exists

    @staticmethod
    def exists_email(user_id, email):
        user_found = User.query.filter(User.email == email).first()
        user_email_exist = False
        if (user_found):
            user_email_exist = True
            # Si estoy editando un usuario tengo un user_id, si ese user_id es igual al encontrado, no valido el email duplicado.
            if(user_id):
                if(int(user_id) == int(user_found.id)):
                   user_email_exist = False
        return user_email_exist

    @staticmethod
    def get(email):
        return User.query.filter(User.email == email).first()