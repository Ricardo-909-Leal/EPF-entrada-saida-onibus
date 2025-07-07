import json
import os
from models.user import UserModel

class AuthService:
    def __init__(self):
        self.usuarios_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'usuarios.json')
        self.usuarios = self._carregar_usuarios()

    def _carregar_usuarios(self):
        if not os.path.exists(self.usuarios_path):
            return []
        with open(self.usuarios_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def autenticar(self, usuario, senha):
        user_model = UserModel()
        return user_model.authenticate(usuario, senha)


