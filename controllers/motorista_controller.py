from bottle import Bottle, request
from controllers.base_controller import BaseController
from services.motorista_service import MotoristaService

class MotoristaController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.service = MotoristaService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/motoristas', method='GET', callback=self.listar)
        self.app.route('/motoristas/add', method=['GET', 'POST'], callback=self.adicionar)
        self.app.route('/motoristas/edit/<cpf>', method=['GET', 'POST'], callback=self.editar)
        self.app.route('/motoristas/delete/<cpf>', method='POST', callback=self.deletar)
    
    def listar(self):
        print("Chamou listar motoristas")
        motoristas = self.service.get_all()
        return self.render('motoristas', motoristas=motoristas)

    def adicionar(self):
        if request.method == 'GET':
            return self.render('motorista_form', motorista=None, action='/motoristas/add')
        else:
            self.service.save()
            self.redirect('/motoristas')

    def editar(self, cpf):
        motorista = self.service.get_by_cpf(cpf)
        if not motorista:
            return "Motorista não encontrado", 404

        if request.method == 'GET':
            return self.render('motorista_form', motorista=motorista, action=f'/motoristas/edit/{cpf}')
        else:
            self.service.edit_motorista(motorista)
            self.redirect('/motoristas')

    def deletar(self, cpf):
        self.service.delete_motorista(cpf)
        self.redirect('/motoristas')


# Para o main.py
motorista_routes = Bottle()
motorista_controller = MotoristaController(motorista_routes)
