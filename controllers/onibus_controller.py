from bottle import Bottle, request
from .base_controller import BaseController
from services.onibus_service import OnibusService

class OnibusController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.onibus_service = OnibusService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/onibus', method='GET', callback=self.list_onibus)
        self.app.route('/onibus/add', method=['GET', 'POST'], callback=self.add_onibus)
        self.app.route('/onibus/edit/<onibus_id>', method=['GET', 'POST'], callback=self.edit_onibus)
        self.app.route('/onibus/delete/<onibus_id>', method='POST', callback=self.delete_onibus)
        self.app.route('/onibus/finalizar/<onibus_id>', method=['GET', 'POST'], callback=self.finalizar_viagem)

    def list_onibus(self):
        self.require_login()
        lista = self.onibus_service.get_all()

        for o in lista:
            o.nome_motorista = self.onibus_service.get_nome_motorista(o.cpf_motorista)
            o.nome_terminal_origem = self.onibus_service.get_nome_terminal(o.id_terminal_origem)
            o.nome_terminal_destino = self.onibus_service.get_nome_terminal(o.id_terminal_destino)

        return self.render('onibus', onibus=lista)


    def add_onibus(self):
        self.require_login()
        if request.method == 'GET':
            motoristas = self.onibus_service.get_motoristas()
            terminais = self.onibus_service.get_terminais()
            return self.render('onibus_form', onibus=None, action="/onibus/add", motoristas=motoristas, terminais=terminais)
        else:
            self.onibus_service.save()
            self.redirect('/onibus')

    def edit_onibus(self, onibus_id):
        self.require_login()
        onibus = self.onibus_service.get_by_id(onibus_id)
        if not onibus:
            return "Ônibus não encontrado", 404

        if request.method == 'GET':
            motoristas = self.onibus_service.get_motoristas()
            terminais = self.onibus_service.get_terminais()
            return self.render('onibus_form', onibus=onibus, action=f"/onibus/edit/{onibus_id}", motoristas=motoristas, terminais=terminais)
        else:
            self.onibus_service.edit_onibus(onibus)
            self.redirect('/onibus')

    def delete_onibus(self, onibus_id):
        self.require_login()
        self.onibus_service.delete_onibus(onibus_id)
        self.redirect('/onibus')
        
    def finalizar_viagem(self, onibus_id):
        self.require_login()
        onibus = self.onibus_service.get_by_id(onibus_id)

        if not onibus:
            return "Ônibus não encontrado", 404

        if request.method == 'GET':
            # Mostra formulário para inserir número de passagens
            return self.render('finalizar_viagem_form', onibus=onibus)
        else:
            passagens = request.forms.get('passagens')
            try:
                passagens = int(passagens)
            except (ValueError, TypeError):
                return "Número de passagens inválido", 400

            self.onibus_service.encerrar_viagem(onibus_id, passagens)
            self.redirect('/onibus')


onibus_routes = Bottle()
onibus_controller = OnibusController(onibus_routes)
