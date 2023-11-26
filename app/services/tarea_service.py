
from app.models import Tarea
from app.repositories import TareaRepository


class TareaService:
    def __init__(self):
        self.repository = TareaRepository()

    def get_all(self) -> list[Tarea]:
        return self.repository.get_all()

    def get_by_id(self, id)-> Tarea:
        return self.repository.get_by_id(id)

    def create(self, entity: Tarea)-> Tarea:
        return self.repository.create(entity)

    def update(self, id, tarea) -> Tarea:
        return self.repository.update(id, tarea)

    def delete(self, id)->bool:
        return self.repository.delete(id)