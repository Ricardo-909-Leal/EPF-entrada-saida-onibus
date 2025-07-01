from bottle import request
from models.terminal import Terminal, TerminalModel

class TerminalService:
    def __init__(self):
        self.model = TerminalModel()

    def get_all(self):
        return self.model.get_all()

    def get_by_id(self, terminal_id):
        return self.model.get_by_id(terminal_id)

    def save(self):
        last_id = max([int(t.id) for t in self.model.get_all()], default=0)
        new_id = str(last_id + 1)

        nome = request.forms.get('nome')
        endereco = request.forms.get('endereco')
        capacidade = request.forms.get('capacidade')

        terminal = Terminal(
            id=new_id,
            nome=nome,
            endereco=endereco,
            capacidade=capacidade
        )
        self.model.add_terminal(terminal)

    def edit_terminal(self, terminal):
        terminal.nome = request.forms.get('nome')
        terminal.endereco = request.forms.get('endereco')
        terminal.capacidade = request.forms.get('capacidade')

        self.model.update_terminal(terminal)

    def delete_terminal(self, terminal_id):
        self.model.delete_terminal(terminal_id)
