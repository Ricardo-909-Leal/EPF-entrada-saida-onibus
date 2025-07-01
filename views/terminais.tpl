

<h2>Lista de Terminais</h2>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Localização</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
        % if terminais:
            % for t in terminais:
                <tr>
                    <td>{{t.id}}</td>
                    <td>{{t.nome}}</td>
                    <td>{{t.endereco}}</td>
                    <td>
                        <a href="/terminais/edit/{{t.id}}">Editar</a>
                        <form action="/terminais/delete/{{t.id}}" method="post" style="display:inline;">
                            <button type="submit" onclick="return confirm('Confirmar exclusão?')">Excluir</button>
                        </form>
                    </td>
                </tr>
            % end
        % else:
            <tr><td colspan="4">Nenhum terminal cadastrado.</td></tr>
        % end
    </tbody>
</table>

<p><a class="button" href="/terminais/add">Adicionar Novo Terminal</a></p>
