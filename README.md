# dajngo

Projeto Django Elden Ring CRUD + API
Este projeto Django demonstra um CRUD completo para Guildas e Personagens, com consumo de API externa do Elden Ring.

Funcionalidades
Template Views: CRUD para Guildas e Personagens usando templates HTML com Jinja.
Autenticação: Login/logout para usuários. CRUD restrito a funcionários (is_staff).
Busca: Campos de busca em listas de Guildas e Personagens.
API REST: Endpoints para Guildas/Personagens com autenticação JWT.
Consumo de API Externa: Busca de criaturas na API do Elden Ring (https://docs.eldenring.fanapis.com/).
Admin em Português: Interface administrativa traduzida.
Instalação
Clone ou baixe o projeto.
Crie um virtualenv: python -m venv myworld
Ative: myworld\Scripts\activate (Windows)
Instale dependências: pip install -r requirements.txt
Banco de Dados
Por padrão, usa SQLite. Para produção, configure PostgreSQL em settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'elden_demo',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Instale PostgreSQL e crie o banco.

Execução
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser (usuário admin, marque como staff)
python manage.py runserver
Acesse: http://127.0.0.1:8000/

Usuários
Público: Pode visualizar Guildas/Personagens e buscar na API externa.
Funcionários (is_staff): Podem criar/editar/excluir Guildas/Personagens.
Login: /login/, Logout: /logout/
admin/admin123 o login inicial
API Endpoints
Templates: / (home), /guilds/, /characters/, /eldenring/ (busca API).
API: /api/guilds/, /api/characters/, /api/token/ (obter token JWT).
Boas Práticas
Estrutura MVC com Django.
Autenticação JWT para API, sessions para templates.
Tratamento de erros.
Templates organizados com base.html.
Dependências
Django 6.0.3
DRF + JWT
Requests
Psycopg2 (para PostgreSQL)