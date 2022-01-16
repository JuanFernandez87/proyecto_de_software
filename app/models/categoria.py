from app.db import db
from sqlalchemy import Column, Integer, String, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

class Categoria(db.Model):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), unique=True)

    def __init__(self, name=None):
        self.name = name
        
    @staticmethod
    def all():
        return Categoria.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Categoria.query.get(id)