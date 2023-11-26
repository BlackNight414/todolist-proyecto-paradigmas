
from app.models import Usuario
from app.repositories import UsuarioRepository


class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def get_all(self) -> list[Usuario]:
        return self.repository.get_all()
