from bottle import Bottle, request, response, redirect, template
from services.auth_service import AuthService

auth_routes = Bottle()
auth_service = AuthService()

@auth_routes.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.forms.get('usuario')
        senha = request.forms.get('senha')

        user = auth_service.autenticar(usuario, senha)
        if user:
            response.set_cookie('usuario', user['usuario'])
            response.set_cookie('tipo', user['tipo'])
            redirect('/')
        else:
            return template('login', erro='Usuário ou senha inválidos.')

    return template('login', erro='')

@auth_routes.route('/logout')
def logout():
    response.delete_cookie('usuario')
    response.delete_cookie('tipo')
    redirect('/login')
