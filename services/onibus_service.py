from bottle import request
from models.onibus import OnibusModel, Onibus

class OnibusService:
    def __init__(self):
        self.onibus_model = OnibusModel()

    def get_all(self):
        return self.onibus_model.get_all()

    def save(self):
        new_id = self.onibus_model.get_next_id() 

        placa = request.forms.get('placa')
        linha = request.forms.get('linha')
        horario_chegada = request.forms.get('horario_chegada')
        horario_saida = request.forms.get('horario_saida')
        terminal = request.forms.get('terminal')

        onibus = Onibus(
            id=new_id,
            placa=placa,
            linha=linha,
            horario_chegada=horario_chegada,
            horario_saida=horario_saida,
            terminal=terminal
        )

        self.onibus_model.add_onibus(onibus)

    def get_by_id(self, onibus_id):
        return self.onibus_model.get_by_id(onibus_id)

    def edit_onibus(self, onibus):
        onibus.placa = request.forms.get('placa')
        onibus.linha = request.forms.get('linha')
        onibus.horario_chegada = request.forms.get('horario_chegada')
        onibus.horario_saida = request.forms.get('horario_saida')
        onibus.terminal = request.forms.get('terminal')

        self.onibus_model.update_onibus(onibus)

    def delete_onibus(self, onibus_id):
        self.onibus_model.delete_onibus(onibus_id)
