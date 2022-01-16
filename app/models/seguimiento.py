from datetime import date
from sqlalchemy.sql.expression import desc

from sqlalchemy.sql.functions import user
from app.db import db
from sqlalchemy import Column, Integer, String, Date
from flask import session
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import query
from datetime import date
from app.models.denuncia import Denuncia

from app.models.user import User
from app.resources import denuncia
class Seguimiento(db.Model):
    __tablename__ = "seguimientos"
    id = Column(Integer, primary_key=True , autoincrement=True)
    descripcion = Column(String(50))
    user_name = Column(String(30))
    fecha = Column(Date)

    def __init__(self, descripcion=None, user_name=None, fecha=None):
        self.descripcion = descripcion
        self.user_name = user_name
        self.fecha = fecha

    def save(self):
        if not self.id:
            db.session.add(self)
            db.session.commit()  

    @staticmethod
    def new_seguimiento(seguimiento, user_name, id_denuncia):
        fecha = date.today()
        seguimiento.fecha = fecha
        seguimiento.user_name = user_name
        denuncia = Denuncia.get_by_id(id_denuncia)
        denuncia.seguimientos.append(seguimiento)
        if seguimiento:
            seguimiento.save()  
    
    @staticmethod
    def all():
        return Seguimiento.query.all()          

    @staticmethod
    def all_paginated(page, per_page, order):
        sort_order = Seguimiento.fecha.asc() if order else Seguimiento.fecha_creacion.desc()
        return Seguimiento.query.filter(Seguimiento.fecha).order_by(sort_order).paginate(page, per_page, error_out=False)        