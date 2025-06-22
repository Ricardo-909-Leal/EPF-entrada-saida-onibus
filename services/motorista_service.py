from bottle import request
from models.motorista import MotoristaModel, Motorista

class MotoristaService:
    def __init__(self):
        self.motorista_model = MotoristaModel()

    def get_all(self):
        return self.motorista_model.get_all()

    def save(self):
        cpf = request.forms.get('cpf')
        nome = request.forms.get('nome')
        cnh = request.forms.get('cnh')
        empresa = request.forms.get('empresa')

        motorista = Motorista(cpf=cpf, nome=nome, cnh=cnh, empresa=empresa)
        self.motorista_model.add_motorista(motorista)

    def get_by_cpf(self, cpf):
        return self.motorista_model.get_by_cpf(cpf)

    def edit_motorista(self, motorista):
        motorista.nome = request.forms.get('nome')
        motorista.cnh = request.forms.get('cnh')
        motorista.empresa = request.forms.get('empresa')
        self.motorista_model.update_motorista(motorista)

    def delete_motorista(self, cpf):
        self.motorista_model.delete_motorista(cpf)
