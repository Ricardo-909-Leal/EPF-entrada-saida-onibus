<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Bottle - {{title or 'Sistema'}}</title>
    <link rel="stylesheet" href="/static/css/style.css" />
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        nav {
            background-color: #333;
            padding: 10px;
        }
        nav ul {
            list-style: none;
            margin: 0;
            padding: 0;
            display: flex;
        }
        nav ul li {
            margin-right: 15px;
        }
        nav ul li a {
            color: #fff;
            text-decoration: none;
        }
        nav ul li a:hover {
            text-decoration: underline;
        }
        .container {
            padding: 20px;
            background-color: #fff;
            min-height: 80vh;
        }
        footer {
            text-align: center;
            padding: 15px;
            background-color: #ddd;
        }
    </style>
</head>
<body>

    <nav>
        <ul>
            <li><a href="/">Início</a></li>
            <li><a href="/onibus">Ônibus</a></li>
            <li><a href="/motoristas">Motoristas</a></li>
            <li><a href="/fiscais">Fiscais</a></li>
            <li><a href="/terminais">Terminais</a></li>
            <li><a href="/users">Usuários</a></li>
        </ul>
    </nav>

    <div class="container">
        {{!base}}  <!-- Aqui entra o conteúdo das páginas filhas -->
    </div>

    <footer>
        <p>&copy; 2025, Meu Projeto. Todos os direitos reservados.</p>
    </footer>

    <!-- Scripts JS no final do body -->
    <script src="/static/js/main.js"></script>
</body>
</html>
