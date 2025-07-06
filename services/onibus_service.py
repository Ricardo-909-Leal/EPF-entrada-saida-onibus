from bottle import request
from models.onibus import OnibusModel, Onibus
from models.motorista import MotoristaModel
from models.terminal import TerminalModel
from datetime import datetime

class OnibusService:
    def __init__(self):
        self.onibus_model = OnibusModel()
        self.motorista_model = MotoristaModel()
        self.terminal_model = TerminalModel()

    def get_all(self):
        onibus_list = self.onibus_model.get_all()
        motorista_model = MotoristaModel()
        terminal_model = TerminalModel()

        for o in onibus_list:
            motorista = motorista_model.get_by_cpf(o.cpf_motorista)
            origem = terminal_model.get_by_id(o.id_terminal_origem)
            destino = terminal_model.get_by_id(o.id_terminal_destino)

            o.motorista_nome = motorista.nome if motorista else 'Desconhecido'
            o.origem_nome = origem.nome if origem else 'Desconhecido'
            o.destino_nome = destino.nome if destino else 'Desconhecido'

        return onibus_list

    def get_motoristas(self):
        return self.motorista_model.get_all()

    def get_terminais(self):
        return self.terminal_model.get_all()

    def save(self):
        new_id = self.onibus_model.get_next_id() 

        placa = request.forms.get('placa')
        linha = request.forms.get('linha')
        horario_chegada = request.forms.get('horario_chegada')
        horario_saida = request.forms.get('horario_saida')
        terminal = request.forms.get('terminal')
        cpf_motorista = request.forms.get('cpf_motorista')
        id_terminal_origem = request.forms.get('id_terminal_origem')
        id_terminal_destino = request.forms.get('id_terminal_destino')
        previsao_chegada = request.forms.get('previsao_chegada')

        onibus = Onibus(
            id=new_id,
            placa=placa,
            linha=linha,
            horario_chegada=horario_chegada,
            horario_saida=horario_saida,
            terminal=terminal,
            id_terminal_origem=id_terminal_origem,
            id_terminal_destino=id_terminal_destino,
            cpf_motorista=cpf_motorista,
            previsao_chegada=previsao_chegada
        )

        self.onibus_model.add_onibus(onibus)

    def get_by_id(self, onibus_id):
        return self.onibus_model.get_by_id(onibus_id)

    def get_nome_motorista(self, cpf):
        motoristas = self.get_motoristas()
        for m in motoristas:
            if m.cpf == cpf:
                return m.nome
        return 'Desconhecido'

    def get_nome_terminal(self, terminal_id):
        terminais = self.get_terminais()
        for t in terminais:
            if t.id == terminal_id:
                return t.nome
        return 'Desconhecido'

    def edit_onibus(self, onibus):
        onibus.placa = request.forms.get('placa')
        onibus.linha = request.forms.get('linha')
        onibus.horario_chegada = request.forms.get('horario_chegada')
        onibus.horario_saida = request.forms.get('horario_saida')
        onibus.terminal = request.forms.get('terminal')
        onibus.cpf_motorista = request.forms.get('cpf_motorista')
        onibus.id_terminal_origem = request.forms.get('id_terminal_origem')
        onibus.id_terminal_destino = request.forms.get('id_terminal_destino')
        onibus.previsao_chegada = request.forms.get('previsao_chegada')

        self.onibus_model.update_onibus(onibus)

    def delete_onibus(self, onibus_id):
        self.onibus_model.delete_onibus(onibus_id)

    def calcular_diferenca(self, onibus: Onibus):
        if not onibus.data_chegada or not onibus.previsao_chegada:
            return "Sem dados suficientes"

        atual = datetime.strptime(onibus.data_chegada, "%Y-%m-%d %H:%M")
        previsto = datetime.strptime(onibus.previsao_chegada, "%Y-%m-%d %H:%M")

        diferenca = atual - previsto
        minutos = int(diferenca.total_seconds() / 60)

        if minutos > 0:
            return f"Atrasado em {minutos} minutos"
        elif minutos < 0:
            return f"Adiantado em {-minutos} minutos"
        else:
            return "Chegou no horário"

    def iniciar_viagem(self, id):
        onibus = self.get_by_id(id)
        if not onibus:
            print(f"Ônibus id={id} não encontrado")
            return False
        if onibus.status != 'esperando':
            print(f"Ônibus id={id} está com status {onibus.status} e não pode iniciar viagem")
            return False
        onibus.status = 'em viagem'
        # Atualiza a hora de saída, por exemplo
        onibus.horario_saida = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.onibus_model.update_onibus(onibus)
        return True


    def encerrar_viagem(self, onibus_id, passagens):
        onibus = self.get_by_id(int(onibus_id))  # converte para inteiro se necessário
        if not onibus:
            print("Ônibus não encontrado")
            return False

        onibus.status = 'chegado'
        onibus.data_chegada = datetime.now().strftime("%Y-%m-%d %H:%M")
        onibus.passagens = passagens

        self.onibus_model.update_onibus(onibus)
        return True
