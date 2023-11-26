from app.models import Usuario
from app import db

class UsuarioRepository:
    def __init__(self):
        self.__model = Usuario

    def get_all(self) -> list[Usuario]:
        return db.session.query(self.__model).all()
