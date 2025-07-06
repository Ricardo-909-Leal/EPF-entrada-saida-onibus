from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.user_service = UserService()


    def setup_routes(self):
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)


    def list_users(self):
        users = self.user_service.get_all()
        return self.render('users', users=users)


    def add_user(self):
        if request.method == 'GET':
            return self.render('user_form', user=None, action="/users/add", erro=None)
        else: 
            try:
                self.user_service.save()  # Só isso, pois já está tratando tudo no service
                self.redirect('/users')

            except ValueError as e:
                return self.render('user_form', user=None, action="/users/add", erro=str(e))

    def edit_user(self, user_id):
        self.require_login()
        user = self.user_service.get_by_id(user_id)
        password = request.forms.get('password')
        if password:
            user.password = password

        if not user:
            return "Usuário não encontrado"

        if request.method == 'GET':
            return self.render(
                'user_form',
                user=user,
                action=f"/users/edit/{user_id}",
                erro=None 
            )
        else:
            try:
                self.user_service.edit_user(user)
                self.redirect('/users')
            except ValueError as e:
                return self.render(
                    'user_form',
                    user=user,
                    action=f"/users/edit/{user_id}",
                    erro=str(e)
                )



    def delete_user(self, user_id):
        self.require_login()
        self.user_service.delete_user(user_id)
        self.redirect('/users')


user_routes = Bottle()
user_controller = UserController(user_routes)
