<h2>
    % if onibus:
        Editar Ônibus
    % else:
        Adicionar Novo Ônibus
    % end
</h2>

<form action="{{action}}" method="post">
    <label>Placa:<br>
        <input type="text" name="placa" required value="{{onibus.placa if onibus else ''}}">
    </label><br><br>

    <label>Linha:<br>
        <input type="text" name="linha" required value="{{onibus.linha if onibus else ''}}">
    </label><br><br>

    <label>Horário de Chegada:<br>
        <input type="time" name="horario_chegada" required value="{{onibus.horario_chegada if onibus else ''}}">
    </label><br><br>

    <label>Horário de Saída:<br>
        <input type="time" name="horario_saida" required value="{{onibus.horario_saida if onibus else ''}}">
    </label><br><br>

    <label>Terminal:<br>
        <input type="text" name="terminal" required value="{{onibus.terminal if onibus else ''}}">
    </label><br><br>

    <button type="submit">Salvar</button>
    <a href="/onibus">Cancelar</a>
</form>
