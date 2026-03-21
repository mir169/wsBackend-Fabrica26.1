# Django Elden Ring API

Projeto Django Elden Ring CRUD + API
Este projeto Django demonstra um CRUD completo para Guildas e Personagens, com consumo robusto da API do Elden Ring.

## Funcionalidades

### 🏰 Sistema CRUD
- **Template Views**: CRUD completo para Guildas e Personagens usando templates HTML com Jinja
- **Autenticação**: Login/logout para usuários. CRUD restrito a funcionários (is_staff)
- **Busca**: Campos de busca em listas de Guildas e Personagens
- **API REST**: Endpoints para Guildas/Personagens com autenticação JWT

### ⚔️ API Elden Ring
- **Busca de Personagens**: Busca específica por nome na API do Elden Ring
- **Listagem Completa**: Visualizar todos os personagens, armas e chefes
- **Dados Offline**: Sistema de fallback com dados mock quando API estiver indisponível
- **Interface Amigável**: Templates responsivos com cards e navegação intuitiva

### 🛡️ Recursos Técnicos
- **Admin em Português**: Interface administrativa traduzida
- **Docker Support**: Configuração completa com Docker Compose
- **PostgreSQL**: Suporte a banco de dados PostgreSQL para produção
- **Boas Práticas**: Estrutura MVC com Django, autenticação JWT para API

## Instalação

```bash
# Clone ou baixe o projeto
git clone <repo-url>
cd dajngo

# Crie virtualenv
python -m venv myworld
myworld\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt
```

## Banco de Dados

Por padrão, usa SQLite. Para produção, configure PostgreSQL em `settings.py`:

```python
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
```

## Execução

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # usuário admin, marque como staff
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

## Docker

```bash
# Construir e executar
make docker-up

# Ou manualmente
docker compose up --build
```

## Usuários

- **Público**: Pode visualizar Guildas/Personagens e explorar API Elden Ring
- **Funcionários (is_staff)**: Podem criar/editar/excluir Guildas/Personagens
- **Login**: `/login/`, **Logout**: `/logout/`
- **Admin inicial**: `admin` / `admin123`

## URLs Disponíveis

### Templates (Interface Web)
- `/` - Página inicial
- `/guilds/` - Listar Guildas
- `/characters/` - Listar Personagens
- `/login/` - Login
- `/logout/` - Logout

### API Elden Ring
- `/eldenring/` - Buscar personagens específicos
- `/eldenring/characters/` - Todos os personagens
- `/eldenring/weapons/` - Armas lendárias
- `/eldenring/bosses/` - Chefes temíveis

### API REST (JSON)
- `/api/guilds/` - CRUD Guildas (JWT required para write)
- `/api/characters/` - CRUD Personagens (JWT required para write)
- `/api/token/` - Obter token JWT

## API Elden Ring - Detalhes

A integração com Elden Ring inclui:

- **Personagens**: Atlan, Melina, Godrick, Rennala, Margit, etc.
- **Armas**: Moonlight Greatsword, Bloody Helix, etc.
- **Chefes**: Godrick the Grafted, Margit the Fell Omen, etc.
- **Fallback**: Dados locais simulados quando API externa estiver offline
- **Status Visual**: Indicadores visuais do status da API

## Arquitetura

- **Backend**: Django 6.0.3 + Django REST Framework
- **Frontend**: Templates HTML + CSS (responsivo)
- **Banco**: SQLite (dev) / PostgreSQL (prod)
- **Autenticação**: Sessions (web) + JWT (API)
- **Container**: Docker + Docker Compose
Tratamento de erros.
Templates organizados com base.html.
Dependências
Django 6.0.3
DRF + JWT
Requests
Psycopg2 (para PostgreSQL)