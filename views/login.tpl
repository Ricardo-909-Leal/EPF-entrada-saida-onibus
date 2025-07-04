<h2 style="text-align:center; margin-top:40px;">Login</h2>

<div style="max-width:350px; margin:40px auto; background:#fff; padding:30px 25px 20px 25px; border-radius:8px; box-shadow:0 2px 8px #0001;">
    % if erro:
        <p style="color:#c00; text-align:center; margin-bottom:20px;">{{erro}}</p>
    % end

    <form method="post" style="display:flex; flex-direction:column; gap:18px;">
        <div>
            <label for="email" style="font-weight:bold;">Email</label>
            <input type="email" id="email" name="email" required style="width:100%; padding:8px; border-radius:4px; border:1px solid #ccc;">
        </div>

        <div>
            <label for="senha" style="font-weight:bold;">Senha</label>
            <input type="password" id="senha" name="senha" required style="width:100%; padding:8px; border-radius:4px; border:1px solid #ccc;">
        </div>

        <button type="submit" style="background:#007bff; color:#fff; border:none; border-radius:4px; padding:10px 0; font-size:16px; cursor:pointer;">
            Entrar
        </button>
    </form>
</div>
