from bottle import Bottle
from bottle import request
from .base_controller import BaseController
from services.onibus_service import OnibusService

class HomeController(BaseController):
    def __init__(self, app: Bottle):
        super().__init__(app)
        self.onibus_service = OnibusService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/home', method='GET', callback=self.home)

    def home(self):
        self.require_login()
        lista = self.onibus_service.get_all()
        tipo_usuario = request.get_cookie('tipo')

        onibus_detalhado = []
        for o in lista:
            situacao = self.onibus_service.calcular_diferenca(o) if o.status == 'chegado' else '-'
            onibus_detalhado.append({
                "id": o.id,
                "placa": o.placa,
                "linha": o.linha,
                "motorista_nome": o.motorista_nome,
                "origem_nome": o.origem_nome,
                "destino_nome": o.destino_nome,
                "status": o.status,
                "previsao_chegada": o.previsao_chegada,
                "data_chegada": o.data_chegada,
                "situacao": situacao
            })

        return self.render('home', onibus=onibus_detalhado, title='Status dos Ônibus', tipo_usuario=tipo_usuario)

home_routes = Bottle()
home_controller = HomeController(home_routes)
