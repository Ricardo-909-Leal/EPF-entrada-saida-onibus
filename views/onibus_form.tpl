
<h2>{{'Editar' if onibus else 'Cadastrar'}} Ônibus</h2>

<form method="post" class="form">
    <label>Placa</label>
    <input type="text" name="placa" value="{{onibus.placa if onibus else ''}}" required>

    <label>Linha</label>
    <input type="text" name="linha" value="{{onibus.linha if onibus else ''}}" required>

    <label>Horário de partida</label>
    <input type="time" name="horario_chegada" value="{{onibus.horario_chegada if onibus else ''}}" required>

    <label>Horário de chegada ao destino</label>
    <input type="time" name="horario_saida" value="{{onibus.horario_saida if onibus else ''}}" required>

    <label>Motorista</label>
    <select name="cpf_motorista" required>
        <option value="">Selecione</option>
        % for m in motoristas:
            <option value="{{m.cpf}}" {{'selected' if onibus and onibus.cpf_motorista == m.cpf else ''}}>
                {{m.nome}} - {{m.cpf}}
            </option>
        % end
    </select>

    <label>Terminal de partida</label>
    <select name="id_terminal_origem" required>
        <option value="">Selecione</option>
        % for t in terminais:
            <option value="{{t.id}}" {{'selected' if onibus and onibus.id_terminal_origem == t.id else ''}}>
                {{t.nome}}
            </option>
        % end
    </select>

    <label>Terminal de Destino</label>
    <select name="id_terminal_destino" required>
        <option value="">Selecione</option>
        % for t in terminais:
            <option value="{{t.id}}" {{'selected' if onibus and onibus.id_terminal_destino == t.id else ''}}>
                {{t.nome}}
            </option>
        % end
    </select>

    <button type="submit" class="btn btn-success">
        {{'Atualizar' if onibus else 'Cadastrar'}}
    </button>
</form>

<p><a href="/onibus" class="btn">Voltar à Lista</a></p>
