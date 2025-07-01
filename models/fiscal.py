import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Fiscal:
    def __init__(self, id, nome, matricula):
        self.id = id
        self.nome = nome
        self.matricula = matricula

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'matricula': self.matricula
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            nome=data['nome'],
            matricula=data['matricula']
        )


class FiscalModel:
    FILE_PATH = os.path.join(DATA_DIR, 'fiscais.json')

    def __init__(self):
        self.fiscais = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Fiscal.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([fiscal.to_dict() for fiscal in self.fiscais], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.fiscais

    def get_by_id(self, fiscal_id):
        return next((f for f in self.fiscais if f.id == fiscal_id), None)

    def get_next_id(self):
        if not self.fiscais:
            return 1
        return max(f.id for f in self.fiscais) + 1

    def add_fiscal(self, fiscal):
        self.fiscais.append(fiscal)
        self._save()

    def update_fiscal(self, fiscal_atualizado):
        for i, fiscal in enumerate(self.fiscais):
            if fiscal.id == fiscal_atualizado.id:
                self.fiscais[i] = fiscal_atualizado
                self._save()
                break

    def delete_fiscal(self, fiscal_id):
        self.fiscais = [f for f in self.fiscais if f.id != fiscal_id]
        self._save()
