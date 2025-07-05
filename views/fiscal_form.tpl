<h2>{{ 'Editar' if fiscal else 'Adicionar' }} Fiscal</h2>

<form action="{{action}}" method="post">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" value="{{fiscal.nome if fiscal else ''}}" required>

    <label for="matricula">Matrícula:</label>
    <input type="text" id="matricula" name="matricula" value="{{fiscal.matricula if fiscal else ''}}" required>

    <label for="terminal_id">Terminal:</label>
    <select id="terminal_id" name="terminal_id" required>
        <option value="">Selecione um terminal</option>
        % for t in terminais:
            <option value="{{t.id}}" {{'selected' if fiscal and fiscal.terminal_id == t.id else ''}}>{{t.nome}}</option>
        % end
    </select>

    <button type="submit" class="btn btn-success">Salvar</button>
    <a href="/fiscais" class="btn">Cancelar</a>
</form>
