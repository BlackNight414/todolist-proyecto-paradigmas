
from app.models import Usuario
from app.repositories import UsuarioRepository


class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def get_all(self) -> list[Usuario]:
        return self.repository.get_all()

    def get_by_id(self, id)-> Usuario:
        return self.repository.get_by_id(id)

    def create(self, entity: Usuario)-> Usuario:
        return self.repository.create(entity)

    def update(self, id, usuario) -> Usuario:
        return self.repository.update(id, usuario)

    def delete(self, id)->bool:
        return self.repository.delete(id)
