from functools import wraps
from bottle import request

def require_login(tipo_necessario=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            usuario, tipo = self.get_usuario_cookie()

            if not usuario:
                return "Você precisa estar logado para acessar esta página.", 403
            
            if tipo_necessario and tipo != tipo_necessario:
                return f"Acesso restrito a usuários do tipo '{tipo_necessario}'.", 403

            return func(self, *args, **kwargs)
        return wrapper
    return decorator
