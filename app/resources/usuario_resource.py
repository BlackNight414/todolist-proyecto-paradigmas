from flask import jsonify, Blueprint, request
from app.mapping import UsuarioSchema
from app.services import UsuarioService

# este usuario lo tengo que declarar en el init de la carpeta
usuario = Blueprint('usuario', __name__)
service = UsuarioService()
usuario_schema = UsuarioSchema()

"""
Obtiene todos los Usuarios
"""
@usuario.route('/', methods=['GET'])
def all():
    # este dump es de la libreria marshmallow y lo convierte en json
    resp = usuario_schema.dump(service.get_all(), many=True) 
    return resp, 200 # Siempre se devuelve 200
