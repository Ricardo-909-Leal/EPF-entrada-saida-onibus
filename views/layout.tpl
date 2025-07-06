<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Bottle - {{title or 'Sistema'}}</title>
    
    <!-- Estilo principal -->
    <link rel="stylesheet" href="/static/css/style.css" />

    <style>
        /* Tipografia e fundo geral */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        /* Navegação superior */
        nav {
            background-color: var(--primary-color);
            padding: 12px 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }

        nav ul {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }

        nav ul li a {
            color: white;
            font-weight: 600;
            text-decoration: none;
            padding: 6px 10px;
            border-radius: 4px;
            transition: background-color 0.3s;
        }

        nav ul li a:hover {
            background-color: var(--secondary-color);
        }

        /* Container central */
        .container {
            max-width: 1200px;
            margin: 30px auto;
            padding: 30px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            min-height: 70vh;
        }

        /* Rodapé */
        footer {
            text-align: center;
            padding: 20px;
            font-size: 0.9rem;
            background-color: #eaeaea;
            color: #666;
            border-top: 1px solid #ccc;
        }
    </style>
</head>
<body>

    <nav>
        <ul>
            <li><a href="/home">Início</a></li>
            <li><a href="/onibus">Ônibus</a></li>
            <li><a href="/motoristas">Motoristas</a></li>
            <li><a href="/fiscais">Fiscais</a></li>
            <li><a href="/terminais">Terminais</a></li>
            <li><a href="/users">Usuários</a></li>

            % if user:
                <li><a href="/logout">Sair ({{user.name}})</a></li>
            % else:
                <li><a href="/login">Login</a></li>
            % end
        </ul>
    </nav>

    <div class="container">
        {{!base}}  <!-- Conteúdo específico de cada página -->
    </div>

    <footer>
        <p>&copy; 2025, Meu Projeto. Todos os direitos reservados.</p>
    </footer>

    <!-- Scripts JS -->
    <script src="/static/js/main.js"></script>
</body>
</html>
