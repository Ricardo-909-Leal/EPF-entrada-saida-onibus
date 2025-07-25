<h2>Lista de Ônibus</h2>

% if mensagem:
<div style="padding:10px; margin-bottom:10px; background-color:#d4edda; color:#155724; border:1px solid #c3e6cb;">
    {{mensagem}}
</div>
% end

<table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <thead>
        <tr style="background-color: #f2f2f2;">
            <th>Placa</th>
            <th>Linha</th>
            <th>Tempo de viagem</th>
            <th>Motorista</th>
            <th>Origem</th>
            <th>Destino</th>
            <th>Status</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
    % if onibus:
        % for o in onibus:
        <tr>
            <td>{{o.placa}}</td>
            <td>{{o.linha}}</td>
            <td>{{o.previsao}}</td>
            <td>{{o.nome_motorista}}</td>
            <td>{{o.nome_terminal_origem}}</td>
            <td>{{o.nome_terminal_destino}}</td>
            <td>{{o.status}}</td>
            <td>
                <div style="display: flex; flex-wrap: wrap; gap: 6px; align-items: center;">
                    <a href="/onibus/edit/{{o.id}}" class="btn btn-success">Editar</a>

                    <form action="/onibus/delete/{{o.id}}" method="post">
                        <button type="submit" class="btn" onclick="return confirm('Confirma exclusão?')">Excluir</button>
                    </form>

                    % if user_tipo == 'motorista' and o.status == 'esperando':
                        <form action="/onibus/iniciar/{{o.id}}" method="post">
                            <button type="submit" class="btn btn-success">Iniciar Viagem</button>
                        </form>
                    % elif user_tipo == 'fiscal' and o.status == 'em viagem':
                        <form action="/onibus/finalizar/{{o.id}}" method="post" style="display: flex; align-items: center; gap: 6px;">
                            <input type="number" name="passagens" min="0" placeholder="Passagens" required style="width: 80px;" />
                            <button type="submit" class="btn btn-danger">Finalizar Viagem</button>
                        </form>
                    % end
                </div>
            </td>
        </tr>
        % end
    % else:
        <tr><td colspan="9">Nenhum ônibus cadastrado.</td></tr>
    % end
    </tbody>
</table>

<p><a href="/onibus/add" class="btn">Adicionar Novo Ônibus</a></p>
