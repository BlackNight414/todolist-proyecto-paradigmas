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
    # print(service.get_all())
    # print(resp)
    return resp, 200 # Siempre se devuelve 200

"""
Obtiene un Usuario por id
"""
@usuario.route('/<int:id>', methods=['GET'])
def one(id):
    resp = usuario_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea un nuevo usuario
"""
@usuario.route('/create', methods=['POST'])
def create():
    usuario = usuario_schema.load(request.json)
    res = usuario_schema.dump(service.create(usuario))
    return resp, 201

"""
Actualiza un Usuario existente
"""
@usuario.route('/<int:id>', methods=['PUT'])
def update(id):
    usuario = usuario_schema.load(request.json)
    resp = usuario_schema.dump(service.update(id, usuario))
    return resp, 200


"""
Elimina un Usuario existente
"""
@usuario.route('/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "Usuario eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el Usuario"
    return jsonify(msg), 204

"""
Filtrar usuarios por apellido
"""
@usuario.route("/<string:apellido>")
def filtrar_apellido(apellido):
    resp = usuario_schema.dump(service.get_all(), many=True) # traemos todo los usuarios (lista donde cada elemento es un diccionario, representando un usuario)
    usuarios_apellido = list(filter(lambda usuario: usuario['apellido']==apellido, resp)) # filtramos por apellido
    #print(usuarios_apellido)
    return usuarios_apellido

"""
Filtrar por apellido e inicial de nombre
""" 
@usuario.route("/<string:apellido>-<string:letra>")
def filtrar1_apellido(apellido, letra):
    resp = usuario_schema.dump(service.get_all(), many=True) 
    usuarios_apellido = list(filter(lambda usuario: usuario['apellido']==apellido and usuario['nombre'].startswith(letra), resp)) # filtramos por apellido y letra inicial de nombre
    return usuarios_apellido