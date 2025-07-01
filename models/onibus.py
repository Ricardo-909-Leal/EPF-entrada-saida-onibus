import json
import os
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Onibus:
    def __init__(self, id, placa, linha, horario_chegada, horario_saida, terminal, id_terminal_origem=None, id_terminal_destino=None, cpf_motorista=None):
        self.id = id
        self.placa = placa
        self.linha = linha
        self.horario_chegada = horario_chegada
        self.horario_saida = horario_saida
        self.terminal = terminal 
        self.id_terminal_origem = id_terminal_origem
        self.id_terminal_destino = id_terminal_destino
        self.cpf_motorista = cpf_motorista
        
        self.motorista_nome = None
        self.origem_nome = None
        self.destino_nome = None

    def to_dict(self):
        return {
            'id': self.id,
            'placa': self.placa,
            'linha': self.linha,
            'horario_chegada': self.horario_chegada,
            'horario_saida': self.horario_saida,
            'terminal': self.terminal,
            'id_terminal_origem': self.id_terminal_origem,
            'id_terminal_destino': self.id_terminal_destino,
            'cpf_motorista': self.cpf_motorista
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            placa=data['placa'],
            linha=data['linha'],
            horario_chegada=data['horario_chegada'],
            horario_saida=data['horario_saida'],
            terminal=data['terminal'],
            id_terminal_origem=data.get('id_terminal_origem'),
            id_terminal_destino=data.get('id_terminal_destino'),
            cpf_motorista=data.get('cpf_motorista')
        )

class OnibusModel:
    FILE_PATH = os.path.join(DATA_DIR, 'onibus.json')

    def __init__(self):
        self.onibus = self._load()

    def _load(self) -> List[Onibus]:
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Onibus.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([o.to_dict() for o in self.onibus], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.onibus

    def get_by_id(self, onibus_id):
        return next((o for o in self.onibus if o.id == onibus_id), None)

    def get_next_id(self):
        if not self.onibus:
            return 1
        return max(o.id for o in self.onibus) + 1

    def add_onibus(self, onibus: Onibus):
        self.onibus.append(onibus)
        self._save()

    def update_onibus(self, updated_onibus: Onibus):
        for i, o in enumerate(self.onibus):
            if o.id == updated_onibus.id:
                self.onibus[i] = updated_onibus
                self._save()
                break

    def delete_onibus(self, onibus_id):
        self.onibus = [o for o in self.onibus if o.id != onibus_id]
        self._save()
