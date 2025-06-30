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

    def list_onibus(self):
        lista_onibus = self.onibus_service.get_all()
        return self.render('onibus', onibus=lista_onibus)

    def add_onibus(self):
        if request.method == 'GET':
            return self.render('onibus_form', onibus=None, action="/onibus/add")
        else:
            self.onibus_service.save()
            self.redirect('/onibus')

    def edit_onibus(self, onibus_id):
        onibus = self.onibus_service.get_by_id(onibus_id)
        if not onibus:
            return "Ônibus não encontrado", 404

        if request.method == 'GET':
            return self.render('onibus_form', onibus=onibus, action=f"/onibus/edit/{onibus_id}")
        else:
            self.onibus_service.edit_onibus(onibus)
            self.redirect('/onibus')

    def delete_onibus(self, onibus_id):
        self.onibus_service.delete_onibus(onibus_id)
        self.redirect('/onibus')

onibus_routes = Bottle()
onibus_controller = OnibusController(onibus_routes)
