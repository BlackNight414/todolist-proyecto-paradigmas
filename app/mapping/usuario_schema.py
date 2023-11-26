from app.models import Usuario
from marshmallow import validate, Schema, fields, post_load

class UsuarioSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=2, max=120))
    apellido = fields.String(required=True, validate=validate.Length(min=2, max=120))
    email = fields.String(required=True, validate=validate.Email())
    password = fields.String(load_only=True)

    @post_load
    def make_usuario(self, data, **kwargs):
        return Usuario(**data)
   