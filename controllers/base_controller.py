from bottle import static_file
from bottle import request, redirect, response

class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()

    def require_login(self):
        usuario = request.get_cookie('usuario')
        if not usuario:
            redirect('/login')
            
    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/', method='GET', callback=self.home_redirect)
        self.app.route('/helper', method=['GET'], callback=self.helper)

        # Rota para arquivos estáticos (CSS, JS, imagens)
        self.app.route('/static/<filename:path>', callback=self.serve_static)


    def home_redirect(self):
        usuario = request.get_cookie('usuario')
        if usuario:
            return self.redirect('/home')
        else:
            return self.redirect('/login')


    def helper(self):
        return self.render('helper-final')


    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        return static_file(filename, root='./static')


    def render(self, template, **context):
        usuario_nome = request.get_cookie('usuario')
        usuario_obj = None
        if usuario_nome:
            from models.user import UserModel
            user_model = UserModel()
            usuario_obj = next((u for u in user_model.get_all() if u.name == usuario_nome), None)
        context['user'] = usuario_obj
        from bottle import template as render_template
        title = context.get('title', 'Sistema')
        context_without_title = {k: v for k, v in context.items() if k != 'title'}
        content = render_template(template, **context_without_title)
        return render_template('layout', base=content, title=title, **context_without_title)




    def redirect(self, path):
        from bottle import redirect as bottle_redirect
        return bottle_redirect(path)

    def set_usuario_cookie(self, nome, tipo):
        response.set_cookie('usuario', nome, path='/')
        response.set_cookie('tipo', tipo, path='/')

    def logout_usuario(self):
        response.delete_cookie('usuario', path='/')
        response.delete_cookie('tipo', path='/')
