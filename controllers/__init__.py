from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.motorista_controller import motorista_routes
from controllers.onibus_controller import onibus_routes
from controllers.fiscal_controller import fiscal_routes
from controllers.terminal_controller import terminal_routes
from controllers.home_controller import home_routes


def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(motorista_routes)
    app.merge(onibus_routes)
    app.merge(fiscal_routes)
    app.merge(terminal_routes)
    app.merge(home_routes)