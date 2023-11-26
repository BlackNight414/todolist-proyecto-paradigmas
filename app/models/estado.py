from app import db
from dataclasses import dataclass

@dataclass
class Estado(db.Model):
    __tablename__ = 'estados'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column('nombre', db.String(120), nullable=False)
    descripcion: str = db.Column('descripcion', db.String(120))
    estados_tareas = db.relationship('Tarea', back_populates='estado', lazy=True)