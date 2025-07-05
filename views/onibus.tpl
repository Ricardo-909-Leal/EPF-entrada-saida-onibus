
<h2>Lista de Ônibus</h2>

<table border="1" cellpadding="5" cellspacing="0">
    <thead>
        <tr>
            <th>Placa</th>
            <th>Linha</th>
            <th>Horário de partida</th>
            <th>Horário de chegada ao destino</th>
            <th>Motorista</th>
            <th>Origem</th>
            <th>Destino</th>
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
            <td>{{o.nome_motorista}}</td>
            <td>{{o.nome_terminal_origem}}</td>
            <td>{{o.nome_terminal_destino}}</td>
            <td>
                <a href="/onibus/edit/{{o.id}}">Editar</a>
                <form action="/onibus/delete/{{o.id}}" method="post" style="display:inline;">
                    <button type="submit" onclick="return confirm('Confirma exclusão?')">Excluir</button>
                </form>
            </td>
        </tr>
        % end
    % else:
        <tr><td colspan="8">Nenhum ônibus cadastrado.</td></tr>
    % end
    </tbody>
</table>

<p><a href="/onibus/add" class="btn">Adicionar Novo Ônibus</a></p>
