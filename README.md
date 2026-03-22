# Django Elden Ring Demo

Projeto Django focado exclusivamente em Elden Ring com CRUD completo do banco de dados e consumo de API externa.

## Funcionalidades

### ⚔️ CRUD Elden Ring (Banco de Dados)
- **Personagens ER DB**: CRUD completo para personagens de Elden Ring armazenados no banco
- **Armas ER DB**: CRUD completo para armas de Elden Ring armazenadas no banco
- **Chefes ER DB**: CRUD completo para chefes de Elden Ring armazenados no banco
- **Busca e Paginação**: Funcionalidades avançadas em todas as listagens
- **Admin Interface**: Gerenciamento através do Django Admin
- **Templates Responsivos**: Interface moderna com tema dark inspirado em Elden Ring

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

- **Público**: Pode visualizar dados da API Elden Ring e ver dados do banco Elden Ring
- **Funcionários (is_staff)**: Podem gerenciar banco de dados Elden Ring (criar/editar/excluir)
- **Login**: `/login/`, **Logout**: `/logout/`
- **Admin inicial**: `admin` / `admin123`

## URLs Disponíveis

### Templates (Interface Web)
- `/` - Página inicial
- `/elden-characters/` - CRUD Personagens Elden Ring (DB)
- `/elden-weapons/` - CRUD Armas Elden Ring (DB)
- `/elden-bosses/` - CRUD Chefes Elden Ring (DB)
- `/login/` - Login
- `/logout/` - Logout

### API Elden Ring
- `/eldenring/` - Buscar personagens específicos
- `/eldenring/characters/` - Todos os personagens
- `/eldenring/weapons/` - Armas lendárias
- `/eldenring/bosses/` - Chefes temíveis

### API REST (JSON)
- `/api/elden-characters/` - CRUD Personagens Elden Ring (JWT required para write)
- `/api/elden-weapons/` - CRUD Armas Elden Ring (JWT required para write)
- `/api/elden-bosses/` - CRUD Chefes Elden Ring (JWT required para write)
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
- **Tema**: Interface dark inspirada em Elden Ring
- **Tratamento de Erros**: Sistema robusto com fallbacks
- **Templates**: Organizados com herança (base.html)

## Dependências

- Django 6.0.3
- Django REST Framework + JWT
- Requests (para API externa)
- Psycopg2 (para PostgreSQL)