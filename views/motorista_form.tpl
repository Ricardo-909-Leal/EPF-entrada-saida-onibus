% include('layout.tpl')

<h2>{{'Editar Motorista' if motorista else 'Cadastrar Motorista'}}</h2>

<form action="{{action}}" method="post">
    <label>CPF:</label><br>
    % if not motorista:
        <input type="text" name="cpf" required><br>
    % else:
        <input type="text" name="cpf" value="{{motorista.cpf}}" readonly><br>
    % end

    <label>Nome:</label><br>
    <input type="text" name="nome" value="{{motorista.nome if motorista else ''}}" required><br>

    <label>CNH:</label><br>
    <input type="text" name="cnh" value="{{motorista.cnh if motorista else ''}}" required><br>

    <label>Empresa:</label><br>
    <input type="text" name="empresa" value="{{motorista.empresa if motorista else ''}}" required><br><br>

    <button type="submit">Salvar</button>
</form>

<a href="/motoristas">Voltar</a>
