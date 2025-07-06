<h1>Status dos Ônibus</h1>

<table class="styled-table">
    <thead>
        <tr>
            <th>ID</th>
            <th>Placa</th>
            <th>Linha</th>
            <th>Motorista</th>
            <th>Origem</th>
            <th>Destino</th>
            <th>Status</th>
            <th>Previsão</th>
            <th>Chegada</th>
            <th>Situação</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
        % for o in onibus:
        <tr>
            <td>{{o['id']}}</td>
            <td>{{o['placa']}}</td>
            <td>{{o['linha']}}</td>
            <td>{{o['motorista_nome']}}</td>
            <td>{{o['origem_nome']}}</td>
            <td>{{o['destino_nome']}}</td>
            <td>{{o['status']}}</td>
            <td>{{o['previsao_chegada'] or '-'}}</td>
            <td>{{o['data_chegada'] or '-'}}</td>
            <td>{{o['situacao']}}</td>
            <td>
                <div style="display: flex; flex-wrap: wrap; gap: 6px; align-items: center;">
                    % if tipo_usuario == 'motorista' and o['status'] == 'esperando':
                        <form action="/onibus/iniciar/{{o['id']}}" method="post">
                            <button type="submit" class="btn btn-success">Iniciar Viagem</button>
                        </form>
                    % elif tipo_usuario == 'fiscal' and o['status'] == 'em viagem':
                        <form action="/onibus/finalizar/{{o['id']}}" method="post" style="display: flex; align-items: center; gap: 6px;">
                            <input type="number" name="passagens" min="0" placeholder="Passagens" required style="width: 70px;" />
                            <button type="submit" class="btn btn-danger">Finalizar Viagem</button>
                        </form>
                    % else:
                        -
                    % end
                </div>
            </td>
        </tr>
        % end
    </tbody>
</table>
