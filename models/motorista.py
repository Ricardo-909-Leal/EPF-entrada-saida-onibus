import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Motorista:
    def __init__(self, cpf, nome, cnh, empresa):
        self.cpf = cpf
        self.nome = nome
        self.cnh = cnh
        self.empresa = empresa

    def __repr__(self):
        return f"Motorista(cpf='{self.cpf}', nome='{self.nome}', empresa='{self.empresa}')"

    def to_dict(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'cnh': self.cnh,
            'empresa': self.empresa
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            cpf=data['cpf'],
            nome=data['nome'],
            cnh=data['cnh'],
            empresa=data['empresa']
        )


class MotoristaModel:
    FILE_PATH = os.path.join(DATA_DIR, 'motoristas.json')

    def __init__(self):
        self.motoristas = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Motorista.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([m.to_dict() for m in self.motoristas], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.motoristas

    def get_by_cpf(self, cpf):
        return next((m for m in self.motoristas if m.cpf == cpf), None)

    def add_motorista(self, motorista):
        self.motoristas.append(motorista)
        self._save()

    def update_motorista(self, motorista_atualizado):
        for i, motorista in enumerate(self.motoristas):
            if motorista.cpf == motorista_atualizado.cpf:
                self.motoristas[i] = motorista_atualizado
                self._save()
                break

    def delete_motorista(self, cpf):
        self.motoristas = [m for m in self.motoristas if m.cpf != cpf]
        self._save()
