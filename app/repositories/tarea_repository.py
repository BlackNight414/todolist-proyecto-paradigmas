from app.models import Tarea
from app import db

class TareaRepository:
    def __init__(self):
        self.__model = Tarea

    def get_all(self) -> list[Tarea]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Tarea:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Tarea) -> Tarea:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Tarea) -> Tarea:
        entity = self.get_by_id(id)
        entity.fecha = t.fecha
        entity.duracion = t.duracion
        entity.descripcion = t.descripcion
        entity.creador_id = t.creador_id
        entity.ejecutante_id = t.ejecutante_id
        entity.categoria_id = t.categoria_id
        entity.estado_id = t.estado_id
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, id)-> bool:
        tarea = self.get_by_id(id)
        db.session.delete(tarea)
        db.session.commit()
        return tarea