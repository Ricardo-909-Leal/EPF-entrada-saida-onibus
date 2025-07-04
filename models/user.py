import json
import os
from dataclasses import dataclass, asdict
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

# Função simples de "hash" (educacional)
def simple_hash(password: str) -> str:
    hashed = ''.join(chr((ord(c) + 5) % 126) for c in password)
    return ''.join(format(ord(c), '02x') for c in hashed)


class User:
    def __init__(self, id, name, email, birthdate, password, tipo="user"):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.password = simple_hash(password) if not self._is_hashed(password) else password
        self.tipo = tipo

    def _is_hashed(self, pwd: str):
        if not pwd or pwd.strip() == "":
            return False
        # Considere hash apenas se for hexadecimal E tiver pelo menos 6 caracteres
        return all(c in '0123456789abcdef' for c in pwd) and len(pwd) >= 6

    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', email='{self.email}', "
                f"birthdate='{self.birthdate}')")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate,
            'password': self.password,
            'tipo': self.tipo
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            birthdate=data['birthdate'],
            password=data.get('password', 'senha123'),  # suporte a dados antigos sem senha
            tipo=data.get('tipo', 'user')
        )

class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.users

    def get_by_id(self, user_id: int):
        return next((u for u in self.users if u.id == user_id), None)

    def get_by_email(self, email: str):
        for user in self.users:
            if user.email.lower() == email.lower():
                return user
        return None

    def add_user(self, user: User):
        self.users.append(user)
        self._save()

    def update_user(self, updated_user: User):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break

    def delete_user(self, user_id: int):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()

    def authenticate(self, email: str, password: str):
        user = self.get_by_email(email)
        print("Tentando autenticar:", email, password)
        print("Usuário encontrado:", user)
        if user:
            print("Senha digitada (hash):", simple_hash(password))
            print("Senha salva:", user.password)
            print("Senha recebida no cadastro:", password)
        if user and user.password == simple_hash(password):
            return user
        return None
