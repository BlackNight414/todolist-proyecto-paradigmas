from flask import jsonify, Blueprint, request
from app.mapping import TareaSchema
from app.services import TareaService

tarea = Blueprint('tarea', __name__)
service = TareaService()
tarea_schema = TareaSchema()

"""
Obtiene todas las Tareas
"""
@tarea.route('/', methods=['GET'])
def all():
    resp = tarea_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una Tarea por id
"""
@tarea.route('/<int:id>', methods=['GET'])
def one(id):
    resp = tarea_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva Tarea
"""
@tarea.route('/', methods=['POST'])
def create():
    tarea = tarea_schema.load(request.json)
    resp = tarea_schema.dump(service.create(tarea))
    return resp, 201

"""
Actualiza una Tarea existente
"""
@tarea.route('/<int:id>', methods=['PUT'])
def update(id):
    tarea = tarea_schema.load(request.json)
    resp = tarea_schema.dump(service.update(id, tarea))
    return resp, 200

"""
Elimina una Tarea existente
"""
@tarea.route('/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "Tarea eliminada correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar la Tarea"
    return jsonify(msg), 204