import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Terminal:
    def __init__(self, id, nome, endereco, capacidade):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.capacidade = capacidade

    def __repr__(self):
        return f"Terminal(id={self.id}, nome='{self.nome}', endereco='{self.endereco}', capacidade={self.capacidade})"

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'capacidade': self.capacidade
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            nome=data['nome'],
            endereco=data['endereco'],
            capacidade=data['capacidade']
        )


class TerminalModel:
    FILE_PATH = os.path.join(DATA_DIR, 'terminais.json')

    def __init__(self):
        self.terminais = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Terminal.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self.terminais], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.terminais

    def get_by_id(self, terminal_id):
        return next((t for t in self.terminais if t.id == terminal_id), None)

    def add_terminal(self, terminal):
        self.terminais.append(terminal)
        self._save()

    def update_terminal(self, updated_terminal):
        for i, terminal in enumerate(self.terminais):
            if terminal.id == updated_terminal.id:
                self.terminais[i] = updated_terminal
                self._save()
                break

    def delete_terminal(self, terminal_id):
        self.terminais = [t for t in self.terminais if t.id != terminal_id]
        self._save()
