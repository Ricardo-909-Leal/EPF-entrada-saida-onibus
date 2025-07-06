

<h2>Lista de Fiscais</h2>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>CPF</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
    % if fiscais:
        % for f in fiscais:
        <tr>
            <td>{{f.id}}</td>
            <td>{{f.nome}}</td>
            <td>{{f.cpf}}</td>
            <td>
                <a href="/fiscais/edit/{{f.id}}">Editar</a>
                <form action="/fiscais/delete/{{f.id}}" method="post" style="display:inline;">
                    <button type="submit" onclick="return confirm('Confirmar exclusão?')">Excluir</button>
                </form>
            </td>
        </tr>
        % end
    % else:
        <tr><td colspan="4">Nenhum fiscal cadastrado.</td></tr>
    % end
    </tbody>
</table>

<p><a href="/fiscais/add">Adicionar Novo Fiscal</a></p>
