from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import query
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, Float
from app.db import db
from sqlalchemy import Column, Integer, String, Boolean

from app.models.coordenada import Coordenada


class Puntos(db.Model):
    __tablename__ = "puntos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), unique=True)
    direccion = Column(String(30))
    estado = Column(Boolean)
    telefono = Column(String(30))
    email = Column(String(30))
    id_coordenada = Column(Integer, ForeignKey('coordenada.id'))

    def __init__(self, nombre: str = None, direccion: str = None ,estado: Boolean = True, telefono: int = None, email: str = None,lat = None,lng = None):
        """Constructor de puntos de encuentro

        Args:
            nombre (str, optional): [description]. Defaults to None.
            direccion (str, optional): [description]. Defaults to None.
            coordenadas (str, optional): [description]. Defaults to None.
            estado (Boolean, optional): 0 == Despublicado 1 == Publicado. Defaults to None.
            telefono (int, optional): [description]. Defaults to None.
            email (str, optional): [description]. Defaults to None.
        """
        self.nombre = nombre
        self.direccion = direccion
        self.estado = estado
        self.telefono = telefono
        self.email = email
    
  
    def save(self):
        """Agrega el punto de encuentro y actualiza la bd
        """
        if not self.id:
            db.session.add(self)
            db.session.commit()

    def remove(self):
        """Borra el punto de encuentro y actualiza la bd
        """
        db.session.delete(self)
        db.session.commit()

    def update(self, values: dict):
        """Actualiza un punto de encuentro

        Args:
            values ([type]): Son los datos nuevos para actualizar
        """
        self.nombre = values.get('nombre')
        self.direccion = values.get('direccion')
        self.estado = True if values.get('estado') == 'SI' else False
        self.telefono = values.get('telefono')
        self.email = values.get('email')
        db.session.commit()

    @staticmethod
    def new_punto(punto):
        if punto:
            punto.save()
            

    @staticmethod
    def buscar_por_valor(valor: str):
        """Formatea el valor pasado como parametro y hace una query con la funcion like

        Args:
            valor (str): [description]

        Returns:
            BaseQuery: [description]
        """
        if valor:
            valor = '%{0}%'.format(valor)
            busqueda = Puntos.query.filter(
                Puntos.nombre.like(valor)).order_by(Puntos.nombre)
        else:
            busqueda = db.session.query(Puntos)

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
            # Para retornar un objeto query necesito hacer esta consulta en vez de llamar a Puntos.all()
            busqueda = db.session.query(Puntos)
        else:
            busqueda = Puntos.query.filter(Puntos.estado == tipo)
        return busqueda

    @staticmethod
    def validar_nombre(punto_id: int, nombre: str) -> Boolean:
        """Validación utilizada por el wtf form para el nombre de punto

        Args:
            punto_id (int): [description]
            nombre (str): [description]

        Returns:
            Boolean: True -> No se puede modificar 
        """
        punto_found = Puntos.query.filter(Puntos.nombre == nombre).first()
        punto_name_exists = False
        if (punto_found):
            punto_name_exists = True
            # Si estoy editando un punto tengo un punto_id, si ese punto_id es igual al encontrado, no valido el nombre del punto duplicado.
            if(punto_id):
                if(int(punto_id) == int(punto_found.id)):
                    punto_name_exists = False
        return punto_name_exists


    
    @staticmethod
    def validar_latitud(punto_id: int,latitud : float) -> Boolean:
        """ Validación utilizada por el wtf form para las coordenadas del punto
        Args:
            punto_id (int): [description]
            latitud (float): [description]

        Returns:
            Boolean: True -> No se puede modificar
        """
        punto_found = Puntos.query.filter(
            Puntos.lat == latitud).first()
        punto_coordenada_exists = False
        if (punto_found):
            punto_coordenada_exists = True
            # Si estoy editando un punto tengo un punto_id, si ese punto_id es igual al encontrado, no valido la coordenada del punto duplicado.
            if(punto_id):
                if(int(punto_id) == int(punto_found.id)):
                    punto_coordenada_exists = False
        return punto_coordenada_exists
    @staticmethod
    def validar_longitud(punto_id: int,longitud: float) -> Boolean:
        """ Validación utilizada por el wtf form para las coordenadas del punto
        Args:
            punto_id (int): [description]
            longitud (float): [description]

        Returns:
            Boolean: True -> No se puede modificar
        """
        punto_found = Puntos.query.filter(
            Puntos.lng == longitud).first()
        punto_coordenada_exists = False
        if (punto_found):
            punto_coordenada_exists = True
            # Si estoy editando un punto tengo un punto_id, si ese punto_id es igual al encontrado, no valido la coordenada del punto duplicado.
            if(punto_id):
                if(int(punto_id) == int(punto_found.id)):
                    punto_coordenada_exists = False
        return punto_coordenada_exists

    def obtener_punto_por_id(id: int) -> query:
        """Utilizado para que mediante un id -> nos devuelva los demas datos

        Args:
            id (int): [description]

        Returns:
            query: ej :<Punto 1> 
        """
        return Puntos.query.get(id)

    def obtener_coordenadas_por_id_de_punto(id: int) -> dict:
        """Utilizado para que mediante un id -> nos devuelva las coordenadas en una lista

        Args:
            id (int): [description]

        Returns:
            coordenadas: dict
        """
        coordenadas = {}
        id_coordenada = Puntos.obtener_punto_por_id(id).id_coordenada
        c = Coordenada.get_by_id(id_coordenada)
        coordenadas["lat"]=c.latitud
        coordenadas["lng"]=c.longitud
        return coordenadas

    def devolver_estados() -> list:
        # PROCESO PARA ACTUALIZAR WTForm los estados, pero no anda todavia
        return db.session.query(Puntos.estado)

    @staticmethod
    def all() -> list:
        """Hace una query devolviendo todos los puntos de encuentro

        Returns:
            list: Retorna una LISTA con todos los puntos de encuentro
        """
        return Puntos.query.all()

    @staticmethod
    def delete(id: int) -> Boolean:
        """Comprueba que el id del punto exista, si existe le manda sus datos(remove) para que sean borrados

        Args:
            id (int): id del punto de encuentro a borrar

        Returns:
            Boolean: Si se realizo la acción
        """
        punto = Puntos.query.get(id)
        if punto:
            punto.remove()
            return True
        return False

    @staticmethod
    def update_punto(id: int, values: dict):
        """Obtiene el punto mediante el id y llama a otro modulo para que lo actualize en la bd con los datos nuevos (values)

        Args:
            id (int): id del punto a actualizar
            values (dict): Son los datos nuevos a actualizar
        """
        punto_update = Puntos.obtener_punto_por_id(id)
        if punto_update:
            punto_update.update(values)
    def obtener_json(puntos : list) -> list:
            """Metodo utilizado para ordenar los datos de la API

            Args:
                puntos (list): [ <Punto1>, ...]

            Returns:
                list: [ {} , {} , {}]
            """
            array_puntos = []
            for punto in puntos:
                coordenadas = Coordenada.get_by_id(punto.id_coordenada)
                json_punto = {
                    "id": punto.id,
                    "nombre": punto.nombre,
                    "dirección": punto.direccion,
                    "lat": coordenadas.latitud,
                    "long": coordenadas.longitud,
                    "telefono": punto.telefono,
                    "email": punto.email
                }
                array_puntos.append(json_punto)
            return array_puntos
