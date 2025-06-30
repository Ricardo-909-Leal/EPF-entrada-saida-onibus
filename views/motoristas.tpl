% title = "Lista de Motoristas"

<h2>Lista de Motoristas</h2>

<table>
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
    % for m in motoristas:
        <tr>
            <td>{{m.cpf}}</td>
            <td>{{m.nome}}</td>
            <td>{{m.cnh}}</td>
            <td>{{m.empresa}}</td>
            <td>
                <a href="/motoristas/edit/{{m.cpf}}" class="btn btn-edit">Editar</a>
                <form action="/motoristas/delete/{{m.cpf}}" method="post" style="display:inline;">
                    <button type="submit" class="btn btn-delete" onclick="return confirm('Confirmar exclusão?')">Excluir</button>
                </form>
            </td>
        </tr>
    % end
    </tbody>
</table>

<a href="/motoristas/add" class="btn btn-success">Adicionar Motorista</a>
