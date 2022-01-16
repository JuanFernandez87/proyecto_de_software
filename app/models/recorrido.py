from operator import ipow
from flask.json import jsonify
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import table
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint, Table
from app.db import db
from sqlalchemy import Column, Integer, String, Boolean
import random
from app.models.coordenada import Coordenada


#one-to-many association table: recorridos - coordenadas
recorridos_coordenadas = Table('recorrido_coordenada', db.metadata,
    Column('id_punto_recorrido', Integer, ForeignKey('recorrido.id', ondelete='CASCADE')),
    Column('id_coordenada', Integer, ForeignKey('coordenada.id', ondelete='CASCADE')),
    PrimaryKeyConstraint('id_punto_recorrido', 'id_coordenada')
)


class Recorrido(db.Model):
    __tablename__ = "recorrido"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30))
    descripcion = Column(String(30))
    estado = Column(Boolean)
    recorrido = relationship(
    'Coordenada',
    secondary=recorridos_coordenadas,
    backref='recorrido_coordenada')
    
    def __init__(self, nombre :str =None, descripcion : str =None, estado : Boolean=None, coordinates : str= None):
        self.nombre = nombre
        self.descripcion  = descripcion 
        self.estado =estado
        
    def save(self):
        if not self.id:
            db.session.add(self)
            db.session.commit()

    def remove(self):
        if self.id:
            db.session.delete(self)
            db.session.commit()
    
    def update(self, values):
        self.nombre = values.get('nombre')
        self.descripcion = values.get('descripcion')
        self.estado = True if values.get('estado') == 'True' else False

        db.session.commit()

    @staticmethod
    def new_recorrido(recorrido):
        if recorrido:
            recorrido.save()

    @staticmethod
    def all():
        return Recorrido.query.all()

    @staticmethod
    def delete_all():
        Recorrido.query.delete()

    @staticmethod
    def delete(id):
        recorrido = Recorrido.query.get(id)
        if recorrido:
            recorrido.remove()
            if(recorrido.recorrido):
                Coordenada.delete_area(recorrido.recorrido)
            return True
        return False
    
    @staticmethod
    def get_by_id(id):
        return Recorrido.query.get(id)

    @staticmethod
    def update_recorrido(id, values):
        recorrido_update = Recorrido.query.get(id)
        if recorrido_update:
            recorrido_update.recorrido = []
            coordenadas = eval(values['coordinates'])
            for coordenada in coordenadas:
                latitud = coordenada["lat"]
                longitud = coordenada["lng"]
                new_coordenada = Coordenada(latitud=latitud, longitud=longitud)
                recorrido_update.recorrido.append(new_coordenada)
            recorrido_update.update(values)
    
    def buscar_por_valor(valor: str):
        """Formatea el valor pasado como parametro y hace una query con la funcion like

        Args:
            valor (str): [description]

        Returns:
            BaseQuery: [description]
        """
        if valor:
            valor = '%{0}%'.format(valor)
            busqueda = Recorrido.query.filter(
                Recorrido.nombre.like(valor)).order_by(Recorrido.nombre)
        else:
            busqueda = db.session.query(Recorrido)

        return busqueda
        
    @staticmethod
    def buscar_por_tipo(tipo: str):
        """Hace una query dependiendo el tipo de busqueda pasado por parametro

        Args:
            tipo (str): [description]

        Returns:
            BaseQuery: [description]
        """
        if tipo == "Todos":
            # Para retornar un objeto query necesito hacer esta consulta en vez de llamar a Recorrido.all()
            busqueda = db.session.query(Recorrido)
        else:
            busqueda = Recorrido.query.filter(Recorrido.estado == tipo)
        return busqueda
    def obtener_json(recorridos : list) -> list:
        """Metodo utilizado para ordenar los datos de la API

        Args:
            recorrido (list): [ <Recorrido>, ...]

        Returns:
            list: [ {} , {} , {}]
        """
        array_recorrido = []
        for recorrido in recorridos:
            array_coordenadas = []
            for coordenada in recorrido.recorrido:
                json_coord = {"lat": coordenada.latitud, "lng": coordenada.longitud}
                array_coordenadas.append(json_coord)
            color  ="#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
            json_recorrido = {
                "id": recorrido.id,
                "nombre": recorrido.nombre,
                "coordenadas": array_coordenadas,
                "descripcion": recorrido.descripcion,
                "color": color
            }
            array_recorrido.append(json_recorrido)
        
        return array_recorrido