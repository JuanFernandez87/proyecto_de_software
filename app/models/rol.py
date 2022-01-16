from app.db import db
from sqlalchemy import Column, Integer, String, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

#one-to-many association table: roles - permisos
roles_permisos = Table('rol_permiso', db.metadata,
    Column('id_rol', Integer, ForeignKey('roles.id', ondelete='CASCADE')),
    Column('id_permiso', Integer, ForeignKey('permission.id', ondelete='CASCADE')),
    PrimaryKeyConstraint('id_rol', 'id_permiso')
)

class Rol(db.Model):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), unique=True)
    permissions = relationship('Permission',
        secondary=roles_permisos,
        backref='rol_permiso')

    def __init__(self, name=None, permission_id = None):
        self.name = name
        self.permission_id = permission_id

    @staticmethod
    def all():
        return Rol.query.all()
    
    @staticmethod
    def get_by_ids(list_ids):
        return Rol.query.filter(Rol.id.in_(list_ids)).all()