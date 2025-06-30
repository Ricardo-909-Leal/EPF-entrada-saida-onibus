
% title = "Formulário de Motorista"

% if motorista:
<h2>Editar Motorista</h2>
% else:
<h2>Adicionar Motorista</h2>
% end

<form action="{{action}}" method="post" class="form">
    <label for="cpf">CPF:</label>
    <input type="text" id="cpf" name="cpf" value="{{motorista.cpf if motorista else ''}}" {{'readonly' if motorista else ''}} required>

    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" value="{{motorista.nome if motorista else ''}}" required>

    <label for="cnh">CNH:</label>
    <input type="text" id="cnh" name="cnh" value="{{motorista.cnh if motorista else ''}}" required>

    <label for="empresa">Empresa:</label>
    <input type="text" id="empresa" name="empresa" value="{{motorista.empresa if motorista else ''}}" required>

    <button type="submit" class="btn btn-success">Salvar</button>
</form>

<a href="/motoristas" class="btn">← Voltar</a>
