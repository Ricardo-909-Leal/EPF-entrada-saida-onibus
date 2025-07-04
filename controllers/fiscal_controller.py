from bottle import Bottle, request
from .base_controller import BaseController
from services.fiscal_service import FiscalService

class FiscalController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.fiscal_service = FiscalService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/fiscais', method='GET', callback=self.listar)
        self.app.route('/fiscais/add', method=['GET', 'POST'], callback=self.adicionar)
        self.app.route('/fiscais/edit/<fiscal_id>', method=['GET', 'POST'], callback=self.editar)
        self.app.route('/fiscais/delete/<fiscal_id>', method='POST', callback=self.deletar)

    def listar(self):
        self.require_login()  # Verifica se o usuário está logado
        fiscais = self.fiscal_service.get_all()
        return self.render('fiscais', fiscais=fiscais, title="Lista de Fiscais")

    def adicionar(self):
        self.require_login()
        if request.method == 'GET':
            return self.render('fiscal_form', fiscal=None, action='/fiscais/add', title="Adicionar Fiscal")
        else:
            self.fiscal_service.save()
            self.redirect('/fiscais')

    def editar(self, fiscal_id):
        self.require_login()
        fiscal = self.fiscal_service.get_by_id(fiscal_id)
        if not fiscal:
            return "Fiscal não encontrado", 404

        if request.method == 'GET':
            return self.render('fiscal_form', fiscal=fiscal, action=f'/fiscais/edit/{fiscal_id}', title="Editar Fiscal")
        else:
            self.fiscal_service.edit_fiscal(fiscal)
            self.redirect('/fiscais')

    def deletar(self, fiscal_id):
        self.require_login()
        self.fiscal_service.delete_fiscal(fiscal_id)
        self.redirect('/fiscais')

# Para usar no init_controllers
fiscal_routes = Bottle()
fiscal_controller = FiscalController(fiscal_routes)
