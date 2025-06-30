% rebase('layout.tpl')

<h2>Lista de Ônibus</h2>

<table border="1" cellpadding="5" cellspacing="0">
    <thead>
        <tr>
            <th>Placa</th>
            <th>Linha</th>
            <th>Horário de Chegada</th>
            <th>Horário de Saída</th>
            <th>Terminal</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
    % if onibus:
        % for o in onibus:
        <tr>
            <td>{{o.placa}}</td>
            <td>{{o.linha}}</td>
            <td>{{o.horario_chegada}}</td>
            <td>{{o.horario_saida}}</td>
            <td>{{o.terminal}}</td>
            <td>
                <a href="/onibus/edit/{{o.id}}">Editar</a>
                <form action="/onibus/delete/{{o.id}}" method="post" style="display:inline;">
                    <button type="submit" onclick="return confirm('Confirma exclusão?')">Excluir</button>
                </form>
            </td>
        </tr>
        % end
    % else:
        <tr><td colspan="6">Nenhum ônibus cadastrado.</td></tr>
    % end
    </tbody>
</table>

<p><a href="/onibus/add">Adicionar Novo Ônibus</a></p>
