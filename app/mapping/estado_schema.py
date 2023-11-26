from app.models import Estado
from marshmallow import validate, fields, Schema, post_load

class EstadoSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True,validate=validate.Length(min=2, max=120))
    descripcion = fields.String()
    estados_tareas = fields.Nested("TareaSchema", many=True, only=("id", "fecha", "duracion", "descripcion"))

    @post_load
    def make_estado(self, data, **kwargs):
        return Estado(**data)
