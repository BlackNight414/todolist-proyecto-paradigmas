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
    #print(service.get_all())
    #print(resp)
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
@tarea.route('/eliminar/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "Tarea eliminada correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar la Tarea"
        print(msg)
    return jsonify(msg), 204

# Filtración de tareas, por categoría
@tarea.route('/categoria/<string:categoria>')
def tareas_por_categoria(categoria):
    tareas = tarea_schema.dump(service.get_all(), many=True)
    tareas_categoria = list(filter(lambda tarea: tarea['categoria']['nombre'] == categoria, tareas))
    return tareas_categoria
    
@tarea.route('/creador/<string:creador>')
def tareas_por_creador(creador):
    tareas = tarea_schema.dump(service.get_all(), many=True) # traemos todas las tareas
    tareas_creador = list(filter(lambda tarea: tarea['creador']['apellido'] == creador, tareas)) # filtramos por usuario
    return tareas_creador

@tarea.route("/ejecutante/<string:ejecutante>")
def tareas_por_ejecutante(ejecutante):
    tareas = tarea_schema.dump(service.get_all(), many = True)
    tareas_ejecutante = list(filter(lambda tarea: tarea ["ejecutante"] ["apellido"] == ejecutante, tareas))
    return tareas_ejecutante

@tarea.route('/estado/<string:estado>')
def tareas_por_estado(estado):
    tareas = tarea_schema.dump(service.get_all(), many=True)
    tareas_estado = list(filter(lambda tarea: tarea['estado']['nombre'] == estado, tareas))
    return tareas_estado