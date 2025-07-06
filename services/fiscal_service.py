from bottle import request
from models.fiscal import FiscalModel, Fiscal
from models.fiscal import FiscalModel, Fiscal

class FiscalService:
    def __init__(self):
        self.model = FiscalModel()

    def get_all(self):
        return self.model.get_all()

    def get_by_id(self, id):
        return self.model.get_by_id(id)

    def save(self, nome, cpf, terminal_id):
        novo_fiscal = Fiscal(
            id=self.model.get_next_id(),
            nome=nome,
            cpf=cpf,
            terminal_id=terminal_id
        )
        self.model.add_fiscal(novo_fiscal)

    def edit_fiscal(self, fiscal_id, nome, cpf, terminal_id):
        fiscal = self.model.get_by_id(fiscal_id)
        if fiscal:
            fiscal.nome = nome
            fiscal.cpf = cpf
            fiscal.terminal_id = terminal_id
            self.model.update_fiscal(fiscal)

    def delete_fiscal(self, id):
        self.model.delete_fiscal(id)
