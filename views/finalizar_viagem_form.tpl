<h2>Finalizar Viagem do Ônibus</h2>

<p><strong>Placa:</strong> {{onibus.placa}}</p>
<p><strong>Linha:</strong> {{onibus.linha}}</p>
<p><strong>Previsão de chegada:</strong> {{onibus.previsao_chegada or "Não informada"}}</p>

% if onibus.data_chegada:
    <p><strong>Data real de chegada:</strong> {{onibus.data_chegada}}</p>
    <p><strong>Status:</strong> {{onibus.calcular_diferenca(onibus)}}</p>
% else:
    <p><strong>Status:</strong> Aguardando chegada</p>
% end

<form action="/onibus/finalizar/{{onibus.id}}" method="post">
    <label for="passagens">Quantidade de passagens registradas:</label><br>
    <input type="number" id="passagens" name="passagens" required><br><br>

    <button type="submit" class="btn btn-success">Finalizar Viagem</button>
</form>

<p><a href="/onibus" class="btn">Voltar à Lista</a></p>
