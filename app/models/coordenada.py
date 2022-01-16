from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float
from app.db import db
from sqlalchemy import Column, Integer


class Coordenada(db.Model):
    __tablename__ = "coordenada"
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitud = Column(Float(30))
    longitud = Column(Float(30))
    punto = relationship('Puntos')

    def __init__(self, latitud=None, longitud=None):
        self.latitud = latitud
        self.longitud = longitud

    def save(self):
        if not self.id:
            db.session.add(self)
            db.session.commit()

    def remove(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()

    def update (self, values: dict):
        """Actualiza la coordenada

        Args:
            values ([type]): Son los datos nuevos para actualizar
        """
        self.latitud = values.get('lat')
        self.longitud = values.get('lng')
        db.session.commit()

    def remove_area(self):
        if self.id:
            db.session.delete(self)
            # db.session.commit()

    @staticmethod
    def new_coordenada(coordenada):
        if coordenada:
            coordenada.save()
    @staticmethod
    def get_by_id(id):
        return Coordenada.query.get(id)
        
    @staticmethod
    def delete(id):
        coordenada = Coordenada.query.get(id)
        if coordenada:
            coordenada.remove()
            return True
        return False
    
    @staticmethod
    def delete_area(area):
        if area:
            for coord in area:
                coord.remove_area()
            db.session.commit()
            return True
        return False
    @staticmethod
    def update_coordenada(id: int, values: dict):
        """Obtiene el punto mediante el id y llama a otro modulo para que lo actualize en la bd con los datos nuevos (values)

        Args:
            id (int): id del punto a actualizar
            values (dict): Son los datos nuevos a actualizar
        """
        coordenada_update = Coordenada.get_by_id(id)
        if coordenada_update:
            coordenada_update.update(values)