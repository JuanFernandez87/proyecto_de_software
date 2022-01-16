import pdb
from sqlalchemy.util.langhelpers import public_factory
from app.db import db
from sqlalchemy import Column, Integer, String, Boolean

class Config_sistema(db.Model):
    #Tipo -> 1: publica, 2: privada
    id = Column(Integer, primary_key=True , autoincrement=True)

    #Orden -> 0: ascendente, 1: descentente
    orden = Column(Boolean)
    cant_elem = Column(Integer)
    color_header = Column(String(20))
    color_footer = Column(String(20))
    color_button = Column(String(20))

    def __init__(self, orden=None, cant_elem=None, color_header=None, color_footer=None, color_button=None):
        self.orden = orden
        self.cant_elem = cant_elem
        self.color_header = color_header
        self.color_footer = color_footer
        self.color_button = color_button

    @staticmethod
    def update(id, orden, cant_elem, color_header, color_footer, color_button):    
         config = Config_sistema.query.get(id)
         if config: 
             config.orden = orden 
             config.cant_elem = cant_elem
             config.color_header = color_header
             config.color_footer = color_footer
             config.color_button = color_button
             config.save() 
         return config      

    def save(self):
         if not self.id:
             db.session.add(self)
         db.session.commit()

    @staticmethod 
    def get_private_config():
        return Config_sistema.query.get(2)
    
    @staticmethod 
    def get_public_config():
        return Config_sistema.query.get(1)