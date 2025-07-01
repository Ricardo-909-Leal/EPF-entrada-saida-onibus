

<h2>{{'Editar' if terminal else 'Adicionar'}} Terminal</h2>

<form action="{{action}}" method="post" class="form">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" value="{{terminal.nome if terminal else ''}}" required>

    <label for="endereco">Localização:</label>
    <input type="text" id="endereco" name="endereco" value="{{terminal.endereco if terminal else ''}}" required>

    <button class="btn-success" type="submit">Salvar</button>
    <a class="btn" href="/terminais">Cancelar</a>
</form>
