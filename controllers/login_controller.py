from bottle import request, Bottle
from models.user import UserModel 
from .base_controller import BaseController

class LoginController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_model = UserModel()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/logout', method='GET', callback=self.logout)

    def login(self):
        if request.method == 'GET':
            return self.render('login', erro=None)
        else:
            email = request.forms.get('email')
            senha = request.forms.get('senha')
            usuario = self.user_model.authenticate(email, senha)

            if usuario:
                self.set_usuario_cookie(usuario.name, getattr(usuario, 'tipo', 'user'))
                return self.redirect('/')
            else:
                return self.render('login', erro="Usuário ou senha inválidos")
    
    def logout(self):
        self.logout_usuario()
        return self.redirect('/login')

login_routes = Bottle()
login_controller = LoginController(login_routes)
