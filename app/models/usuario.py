from app import db
from dataclasses import dataclass

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column('nombre', db.String(120))
    apellido: str = db.Column('apellido', db.String(120))
    email: str = db.Column('email', db.String(120))
    password: str = db.Column('password', db.String(255)) # lo seteamos en 255 porque luego la contraseña se encripta.
    tareas_creador = db.relationship('Tarea', primaryjoin="Usuario.id == Tarea.creador_id", back_populates='creador', lazy=True)
    tareas_ejecutante = db.relationship('Tarea', primaryjoin="Usuario.id == Tarea.ejecutante_id", back_populates='ejecutante', lazy=True)