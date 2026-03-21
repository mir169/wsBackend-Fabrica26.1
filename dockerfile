Instalação
Clone ou baixe o projeto.
Crie um virtualenv: python -m venv myworld
Ative: myworld\Scripts\activate (Windows)
Instale dependências: pip install -r requirements.txt
Banco de Dados
Por padrão, usa SQLite. Para produção, configure PostgreSQL em settings.py:
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