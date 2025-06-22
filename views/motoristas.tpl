% include('layout.tpl')

<h2>Lista de Motoristas</h2>

<a href="/motoristas/add">Adicionar Motorista</a><br><br>

<table border="1" cellpadding="8" cellspacing="0">
    <thead>
        <tr>
            <th>CPF</th>
            <th>Nome</th>
            <th>CNH</th>
            <th>Empresa</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
    % for motorista in motoristas:
        <tr>
            <td>{{motorista.cpf}}</td>
            <td>{{motorista.nome}}</td>
            <td>{{motorista.cnh}}</td>
            <td>{{motorista.empresa}}</td>
            <td>
                <a href="/motoristas/edit/{{motorista.cpf}}">Editar</a> |
                <form action="/motoristas/delete/{{motorista.cpf}}" method="post" style="display:inline;" onsubmit="return confirm('Confirma exclusão?');">
                    <button type="submit">Deletar</button>
                </form>
            </td>
        </tr>
    % end
    </tbody>
</table>

<a href="/">Voltar ao Início</a>
