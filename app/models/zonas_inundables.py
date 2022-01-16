from app.db import db
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from app.models.coordenada import Coordenada
from sqlalchemy.sql.elements import and_

# one-to-many association table: zona_inundable - coordenada
zona_area = Table('zonas_inundable_area', db.metadata,
                  Column('id_zona', Integer, ForeignKey(
                      'zonas_inundables.id', ondelete='CASCADE')),
                  Column('id_coordenada', Integer, ForeignKey(
                      'coordenada.id', ondelete='CASCADE')),
                  PrimaryKeyConstraint('id_zona', 'id_coordenada')
                  )


class Zonas_Inundables(db.Model):
    __tablename__ = "zonas_inundables"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    code = Column(String(32))
    active = Column(Boolean)
    color_capa = Column(String(30))
    cant_puntos = Column(Integer)
    area = relationship(
        'Coordenada',
        secondary=zona_area,
        backref='zona_area')

    def __init__(self, name=None, active=True, code=None, color=None, cant_puntos=0, area=[]):
        self.name = name
        self.code = code
        self.active = active
        self.color_capa = color
        self.cant_puntos = cant_puntos
        self.area = area

    def save(self):
        if not self.id:
            db.session.add(self)
            db.session.commit()

    def remove(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()
    
    def update(self, values):
        self.code = values.get('code')
        self.color_capa = values.get('color_capa')
        self.active = True if values.get('active') else False

        db.session.commit()

    @staticmethod
    def new_zone(zone):
        if zone:
            zone.save()

    @staticmethod
    def all():
        return Zonas_Inundables.query.all()

    @staticmethod
    def all_paginated(page, per_page, order):
        sort_order = Zonas_Inundables.name.desc() if order else Zonas_Inundables.name.asc()
        return Zonas_Inundables.query.filter().order_by(sort_order).paginate(page, per_page, error_out=False)

    @staticmethod
    def delete_all():
        Zonas_Inundables.query.delete()

    @staticmethod
    def delete(id):
        zona = Zonas_Inundables.query.get(id)
        if zona:
            zona.remove()
            if(zona.area):
                Coordenada.delete_area(zona.area)
            return True
        return False
    
    @staticmethod
    def get_by_id(id):
        return Zonas_Inundables.query.get(id)

    @staticmethod
    def update_zona(id, values):
        zona_update = Zonas_Inundables.query.get(id)
        if zona_update:
            zona_update.update(values)

    @staticmethod
    def search(query, page, per_page, order):
        search_array = query.split(",")
        
        name = search_array[0] or ""
        estado = search_array[1] or "1"

        look_for = '%{0}%'.format(name)
        sort_order = Zonas_Inundables.name.desc() if order else Zonas_Inundables.name.asc()
        
        response_query =  Zonas_Inundables.query.filter( and_(Zonas_Inundables.name.like(look_for), Zonas_Inundables.active == estado)).order_by(sort_order)
        return response_query.paginate(page=page, per_page=per_page)
