from app.models import Categoria
from marshmallow import validate, fields, Schema, post_load

class CategoriaSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True)
    descripcion = fields.String()
    tareas = fields.Nested("TareaSchema", many=True, only=("id", "fecha", "duracion", "descripcion"))
    
    @post_load
    def make_categoria(self, data, **kwargs):
        return Categoria(**data)