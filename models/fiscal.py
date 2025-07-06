import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Fiscal:
    def __init__(self, id, nome, cpf, terminal_id=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.terminal_id = terminal_id

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'terminal_id': self.terminal_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            nome=data['nome'],
            cpf=data['cpf'],
            terminal_id=data.get('terminal_id')
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
