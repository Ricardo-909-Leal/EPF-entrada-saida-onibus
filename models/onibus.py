import json
import os
from typing import List
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Onibus:
    def __init__(self, id, placa, linha, horario_chegada, horario_saida, terminal, 
                 id_terminal_origem=None, id_terminal_destino=None, cpf_motorista=None, 
                 status='esperando', data_saida=None, data_chegada=None, passagens=0, 
                 previsao_chegada=None):
        self.id = id
        self.placa = placa
        self.linha = linha
        self.horario_chegada = horario_chegada
        self.horario_saida = horario_saida
        self.terminal = terminal 
        self.id_terminal_origem = id_terminal_origem
        self.id_terminal_destino = id_terminal_destino
        self.cpf_motorista = cpf_motorista
        
        self.status = status  
        self.data_saida = data_saida
        self.data_chegada = data_chegada
        self.passagens = passagens  
        self.previsao_chegada = previsao_chegada  

        
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
            'cpf_motorista': self.cpf_motorista,
            'status': self.status,
            'data_saida': self.data_saida,
            'data_chegada': self.data_chegada,
            'passagens': self.passagens,
            'previsao_chegada': self.previsao_chegada
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
            cpf_motorista=data.get('cpf_motorista'),
            status=data.get('status', 'esperando'),
            data_saida=data.get('data_saida'),
            data_chegada=data.get('data_chegada'),
            passagens=data.get('passagens', 0),
            previsao_chegada=data.get('previsao_chegada')
        )
    
    def calcular_diferenca(self):
        if not self.data_chegada or not self.previsao_chegada:
            return "Sem dados suficientes"

        atual = datetime.strptime(self.data_chegada, "%Y-%m-%d %H:%M")
        previsto = datetime.strptime(self.previsao_chegada, "%Y-%m-%d %H:%M")

        diferenca = atual - previsto
        minutos = int(diferenca.total_seconds() / 60)

        if minutos > 0:
            return f"Atrasado em {minutos} minutos"
        elif minutos < 0:
            return f"Adiantado em {-minutos} minutos"
        else:
            return "Chegou no horário"


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
        onibus_id = int(onibus_id)
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
