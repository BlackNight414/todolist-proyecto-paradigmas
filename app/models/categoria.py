from dataclasses import dataclass
from app import db

@dataclass
class Categoria(db.Model):
    __tablename__ = 'categorias'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column('nombre', db.String(120), nullable=False)
    descripcion: str = db.Column('descripcion', db.String(120))
    tareas = db.relationship('Tarea', back_populates='categoria', lazy=True)

