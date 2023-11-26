from dataclasses import dataclass
from datetime import datetime
from app import db

@dataclass
class Tarea(db.Model):
    __tablename__ = 'tareas'
    id: int = db.Column('id',db.Integer, primary_key=True, autoincrement=True)
    fecha: datetime = db.Column('fecha', db.DateTime, default=datetime.utcnow, nullable=False)
    duracion: datetime = db.Column('duracion', db.Interval, nullable=False)
    descripcion = db.Column('descripcion', db.String(120), nullable=False)

    creador_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    creador = db.relationship("Usuario", foreign_keys=[creador_id]) 

    ejecutante_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    ejecutante = db.relationship("Usuario", foreign_keys=[ejecutante_id])

    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    categoria = db.relationship("Categoria", back_populates='tareas')

    estado_id = db.Column(db.Integer, db.ForeignKey('estados.id'))
    estado = db.relationship("Estado", back_populates='estados_tareas')