from bottle import request
from models.fiscal import FiscalModel, Fiscal

class FiscalService:
    def __init__(self):
        self.fiscal_model = FiscalModel()

    def get_all(self):
        return self.fiscal_model.get_all()

    def save(self):
        last_id = max([int(f.id) for f in self.fiscal_model.get_all()], default=0)
        new_id = str(last_id + 1)

        nome = request.forms.get('nome')
        matricula = request.forms.get('matricula')

        fiscal = Fiscal(
            id=new_id,
            nome=nome,
            matricula=matricula
        )

        self.fiscal_model.add_fiscal(fiscal)

    def get_by_id(self, fiscal_id):
        return self.fiscal_model.get_by_id(fiscal_id)

    def edit_fiscal(self, fiscal):
        nome = request.forms.get('nome')
        matricula = request.forms.get('matricula')

        fiscal.nome = nome
        fiscal.matricula = matricula

        self.fiscal_model.update_fiscal(fiscal)

    def delete_fiscal(self, fiscal_id):
        self.fiscal_model.delete_fiscal(fiscal_id)
