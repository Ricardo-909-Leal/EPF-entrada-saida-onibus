from bottle import request
from models.user import UserModel, User

class UserService:
    def __init__(self):
        self.user_model = UserModel()


    def get_all(self):
        users = self.user_model.get_all()
        return users


    def save(self):
        last_id = max([u.id for u in self.user_model.get_all()], default=0)
        new_id = last_id + 1
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        password = request.forms.get('password')
        if not password:
            # Pode lançar um erro ou retornar uma mensagem amigável
            raise ValueError("Senha não pode ser vazia")
        tipo = request.forms.get('tipo', 'user')

        user = User(id=new_id, name=name, email=email, birthdate=birthdate, password=password, tipo=tipo)
        self.user_model.add_user(user)


    def get_by_id(self, user_id):
        return self.user_model.get_by_id(user_id)


    def edit_user(self, user):
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        tipo = request.forms.get('tipo', 'user')

        user.name = name
        user.email = email
        user.birthdate = birthdate
        user.tipo = tipo

        self.user_model.update_user(user)


    def delete_user(self, user_id):
        self.user_model.delete_user(user_id)
