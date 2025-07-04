from bottle import Bottle, request
from .base_controller import BaseController
from services.terminal_service import TerminalService

class TerminalController(BaseController):
    def __init__(self, app: Bottle):
        super().__init__(app)
        self.service = TerminalService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/terminais', method='GET', callback=self.listar)
        self.app.route('/terminais/add', method=['GET', 'POST'], callback=self.adicionar)
        self.app.route('/terminais/edit/<terminal_id>', method=['GET', 'POST'], callback=self.editar)
        self.app.route('/terminais/delete/<terminal_id>', method='POST', callback=self.deletar)

    def listar(self):
        self.require_login()  # Verifica se o usuário está logado
        terminais = self.service.get_all()
        return self.render('terminais', terminais=terminais, title="Lista de Terminais")

    def adicionar(self):
        self.require_login()
        if request.method == 'GET':
            return self.render('terminal_form', terminal=None, action='/terminais/add', title="Adicionar Terminal")
        else:
            self.service.save()
            self.redirect('/terminais')

    def editar(self, terminal_id):
        self.require_login()
        terminal = self.service.get_by_id(terminal_id)
        if not terminal:
            return "Terminal não encontrado", 404

        if request.method == 'GET':
            return self.render('terminal_form', terminal=terminal, action=f'/terminais/edit/{terminal_id}', title="Editar Terminal")
        else:
            self.service.edit_terminal(terminal)
            self.redirect('/terminais')

    def deletar(self, terminal_id):
        self.require_login()
        self.service.delete_terminal(terminal_id)
        self.redirect('/terminais')


# Rota para registrar no app principal
terminal_routes = Bottle()
terminal_controller = TerminalController(terminal_routes)
