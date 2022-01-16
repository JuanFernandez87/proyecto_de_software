from datetime import date
from app.db import db
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import query
from datetime import date
from app.models.user import User
from random import choice

#one-to-many association table: denuncia - seguimiento
denuncias_seguimiento = Table('denuncia_seguimiento', db.metadata,
    Column('id_denuncia', Integer, ForeignKey('denuncias.id', ondelete='CASCADE')),
    Column('id_seguimiento', Integer, ForeignKey('seguimientos.id', ondelete='CASCADE')),
    PrimaryKeyConstraint('id_denuncia', 'id_seguimiento')
)
class Denuncia(db.Model):
    __tablename__ = "denuncias"
    id = Column(Integer, primary_key=True , autoincrement=True)
    titulo = Column(String(20))
    categoria = Column(Integer)
    fecha_creacion = Column(Date)
    fecha_cierre = Column(Date)
    descripcion = Column(String(50))
    latitud = Column(String(20))
    longitud = Column(String(20))
    # Estados -> Sin confirmar, En curso, Resuelta, Cerrada
    estado = Column(String(20))
    apellido_denunciante = Column(String(20))
    nombre_denunciante = Column(String(20))
    tel_cel_denunciante = Column(String(20))
    # Intentos maximos -> 3, se pasa a Cerrada, "No fue posible contactar al denunciante"
    intentos_comunicacion = Column(Integer)
    email_denunciante = Column(String(20))
    seguimientos = relationship(
        'Seguimiento',
        secondary=denuncias_seguimiento,
        backref='denuncia_seguimiento')    

    def __init__(self, titulo=None, categoria=None, fecha_creacion=None, descripcion=None, latitud=None, longitud=None, estado=None, apellido_denunciante=None, nombre_denunciante=None, tel_cel_denunciante=None, intentos_comunicacion=None, email_denunciante=None, seguimiento_id=None):
        self.titulo = titulo
        self.categoria = categoria
        self.fecha_creacion = fecha_creacion        
        self.fecha_cierre = None
        self.descripcion = descripcion
        self.latitud = latitud
        self.longitud = longitud
        self.estado = estado 
        self.apellido_denunciante = apellido_denunciante
        self.nombre_denunciante = nombre_denunciante
        self.tel_cel_denunciante = tel_cel_denunciante
        self.intentos_comunicacion = intentos_comunicacion
        self.email_denunciante = email_denunciante
        self.seguimiento_id = seguimiento_id

    def save(self):
        if not self.id:
            db.session.add(self)
            db.session.commit()

    @staticmethod
    def new_denuncia(denuncia, id_usuario):
        denuncia.estado = "En curso"
        fecha = date.today()
        denuncia.fecha_creacion = fecha
        denuncia.intentos_comunicacion = 0
        usuario = User.get_by_id(id_usuario)
        usuario.denuncias.append(denuncia)
        if denuncia:
            denuncia.save()  

    def update(self, values):
        self.titulo = values.get('titulo')
        self.categoria = values.get('categoria')
        self.fecha_creacion = values.get('fecha_creacion')        
        self.descripcion = values.get('descripcion')
        self.latitud = values.get('latitud')
        self.longitud = values.get('longitud')
        self.apellido_denunciante = values.get('apellido_denunciante')
        self.nombre_denunciante = values.get('nombre_denunciante')
        self.tel_cel_denunciante = values.get('tel_cel_denunciante')
        self.intentos_comunicacion = values.get('intentos_comunicacion')
        if self.intentos_comunicacion == '3':
            self.estado = 'Cerrada'
            fecha_actual = date.today()
            self.fecha_cierre = fecha_actual
        else:
            self.estado = values.get('estado')
            self.fecha_cierre = values.get('fecha_cierre')              
        self.email_denunciante = values.get('email_denunciante')
        db.session.commit()
    
    @staticmethod
    def update_denuncia(id, values):
        denuncia_update = Denuncia.query.get(id)
        if denuncia_update:
            denuncia_update.update(values)
    # Solo administrador/a tiene permiso para borrar una denuncia
    def delete(id): 
        denuncia = Denuncia.query.get(id)
        if denuncia:
            denuncia.estado = "Eliminado"
            db.session.commit()
            return True        
        return False        

    @staticmethod
    def all():
        return Denuncia.query.all()      

    # Obtengo la lista de la tabla denuncias_seguimiento
    @staticmethod
    def all_seguimientos(id):
        denuncia = Denuncia.get_by_id(id)
        return denuncia.seguimientos
        #return Denuncia.query.order_by(Denuncia.seguimientos == id)             

    @staticmethod
    def all_paginated(page, per_page, order):
        sort_order = Denuncia.fecha_creacion.asc() if order else Denuncia.fecha_creacion.desc()
        return Denuncia.query.filter(Denuncia.fecha_creacion).order_by(sort_order).paginate(page, per_page, error_out=False)
    
    @staticmethod
    def paginar(busqueda: query, page: int, per_page: int, orden: str = "asc") -> BaseQuery.paginate:
        return busqueda.paginate(page=page, per_page=per_page, error_out=False)   

    @staticmethod
    def procesar_busqueda(page: int, per_page: int, orden: str, titulo: str, estado: str, fecha_inicio: str, fecha_fin: str) -> BaseQuery.paginate:        
        denuncias = db.session.query(Denuncia)
        # Si el titulo es distinto de blanco, filtro los titulos y me quedo con las denuncias que coincidan
        if titulo != '':
            denuncias = denuncias.filter(Denuncia.titulo.like(titulo))
        # Si el estado es distinto de todos, filtro los estados y me quedo con las denuncias que coincidan
        if estado != 'Todos':
            denuncias = denuncias.filter(Denuncia.estado.like(estado))
        # Si la fecha es distinta de blanco, filtro las fechas y me quedo con las denuncias que coincidan
        if fecha_inicio != '':            
            denuncias =  denuncias.filter(Denuncia.fecha_creacion >= fecha_inicio)
        if fecha_fin != '':    
            denuncias = denuncias.filter(Denuncia.fecha_creacion <= fecha_fin)            
        denuncias = Denuncia.paginar(denuncias, page, per_page, orden)   
        return denuncias        

    @staticmethod
    def listar_fechas(page: int, per_page: int, orden: str, fechas):
        denuncias = db.session.query(Denuncia)
        denuncias = Denuncia.paginar(denuncias, page, per_page, orden)  
        for denuncia in denuncias.items: 
            fechas.append(denuncia.fecha_creacion)
        fechas = list(set(fechas))   
        return fechas        

    @staticmethod
    def get_by_id(id):
        return Denuncia.query.get(id)      

    def as_dict(self):
        return {attr.name: getattr(self, attr.name) for attr in self.__table__.columns}

    @staticmethod
    def new_denuncia_from_api(denuncia):
        denuncia.estado = "Sin confirmar"
        fecha = date.today()
        denuncia.fecha_creacion = fecha
        denuncia.intentos_comunicacion = 0
        # obtengo una lista con todos los usuarios
        usuarios = db.session.query(User).all()
        # selecciono un usuario random
        id_usuario = choice(range(1, len(usuarios), 1))    
        # le asigno al usuario la denuncia cargada en la API   
        usuario = User.get_by_id(id_usuario)
        usuario.denuncias.append(denuncia)
        # almaceno la denuncia
        if denuncia:
            denuncia.save()          