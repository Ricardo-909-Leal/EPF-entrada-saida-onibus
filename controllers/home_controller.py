from bottle import Bottle
from .base_controller import BaseController

class HomeController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.app.route('/', method='GET', callback=self.home)

    def home(self):
        return self.render('home', title="Página Inicial")

home_routes = Bottle()
home_controller = HomeController(home_routes)
