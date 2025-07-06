from bottle import Bottle, request, abort, response
from bottle import response, redirect
from .base_controller import BaseController
from services.onibus_service import OnibusService
from models.user import User

def require_role(role):
    User.tipo = (request.get_cookie('tipo') or '').lower().strip()
    print("DEBUG - User.tipo =", User.tipo)
    if User.tipo != role:
        abort(403, f"Acesso negado. Apenas {role} pode executar essa ação.")


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
        self.app.route('/onibus/iniciar/<id>', method='POST', callback=self.iniciar_viagem)
        self.app.route('/onibus/finalizar/<id>', method='POST', callback=self.finalizar_viagem)
        
    def list_onibus(self):
        self.require_login()
        lista = self.onibus_service.get_all()
        user_tipo = request.get_cookie('tipo') or ''

        mensagem = request.query.get('msg')
        if mensagem == 'viagem_finalizada':
            mensagem = 'Viagem finalizada com sucesso!'
        else:
            mensagem = None

        for o in lista:
            o.nome_motorista = self.onibus_service.get_nome_motorista(o.cpf_motorista)
            o.nome_terminal_origem = self.onibus_service.get_nome_terminal(o.id_terminal_origem)
            o.nome_terminal_destino = self.onibus_service.get_nome_terminal(o.id_terminal_destino)

        return self.render('onibus', onibus=lista, user_tipo=user_tipo, mensagem=mensagem)

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


    def iniciar_viagem(self, id):
        self.require_login()
        require_role('motorista')
        sucesso = self.onibus_service.iniciar_viagem(id)
        if sucesso:
            response.set_cookie("msg", "Viagem iniciada com sucesso.", path="/")
            return redirect('/onibus')
        else:
            abort(400, "Não foi possível iniciar a viagem.")
  

    def finalizar_viagem(self, id):
        self.require_login()
        require_role('fiscal')

        try:
            passagens = int(request.forms.get('passagens', 0))
        except ValueError:
            return "Número de passagens inválido.", 400

        sucesso = self.onibus_service.encerrar_viagem(id, passagens)
        if sucesso:
            self.redirect('/onibus?msg=viagem_finalizada')
        else:
            return "Não foi possível finalizar a viagem.", 400




onibus_routes = Bottle()
onibus_controller = OnibusController(onibus_routes)
