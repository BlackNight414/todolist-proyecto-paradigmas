from app.models import Tarea
from marshmallow import validate, fields, Schema, post_load

class TareaSchema(Schema):
    id = fields.Integer(dump_only=True)
    fecha = fields.DateTime(required=True)
    duracion = fields.TimeDelta(required=True)
    descripcion = fields.String(required=True)
    creador_id = fields.Integer(required=True)
    ejecutante_id = fields.Integer(required=True)
    categoria_id = fields.Integer(required=True)
    estado_id = fields.Integer(required=True)
    creador = fields.Nested("UsuarioSchema", only=("id", "nombre", "apellido", "email"))
    ejecutante = fields.Nested("UsuarioSchema", only=("id", "nombre", "apellido", "email"))
    categoria = fields.Nested("CategoriaSchema", only=("id", "nombre", "descripcion"))
    estado = fields.Nested("EstadoSchema", only=("id", "nombre", "descripcion"))
    
    @post_load
    def make_tarea(self, data, **kwargs):
        return Tarea(**data)