
<section class="form-section">
    <h1>{{'Editar Usuário' if user else 'Adicionar Usuário'}}</h1>
    
    <form action="{{action}}" method="post" class="form-container">
        <div class="form-group">
            <label for="name">Nome:</label>
            <input type="text" id="name" name="name" required value="{{user.name if user else ''}}">
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required value="{{user.email if user else ''}}">
        </div>
        
        <div class="form-group">
            <label for="birthdate">Data de Nascimento:</label>
            <input type="date" id="birthdate" name="birthdate" required value="{{user.birthdate if user else ''}}">
        </div>

        % if not user:
        <div class="form-group">
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" required>
        </div>
        % end

        <div class="form-group">
            <label for="tipo">Tipo:</label>
            <select id="tipo" name="tipo" required>
                <option value="user" {{'selected' if user and user.tipo == 'user' else ''}}>Usuário</option>
                <option value="admin" {{'selected' if user and user.tipo == 'admin' else ''}}>Administrador</option>
                <option value="fiscal" {{'selected' if user and user.tipo == 'fiscal' else ''}}>Fiscal</option>
                <option value="motorista" {{'selected' if user and user.tipo == 'motorista' else ''}}>Motorista</option>
            </select>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Salvar</button>
            <a href="/users" class="btn-cancel">Voltar</a>
        </div>
    </form>
</section>