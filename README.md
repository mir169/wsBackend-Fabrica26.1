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

Por padrão, usa SQLite. Para produção com Docker, automaticamente usa PostgreSQL.

### Configuração Manual PostgreSQL

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eldendemo',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
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

## Comandos Rápidos (Makefile)

O projeto inclui um Makefile com comandos úteis:

```bash
make help              # Lista todos os comandos disponíveis
make install           # Instala dependências
make makemigrations    # Cria migrações
make migrate           # Aplica migrações
make createsuperuser   # Cria superusuário
make runserver         # Inicia servidor local
make test              # Executa testes
make clean             # Remove arquivos temporários
```

## Docker

O projeto inclui configurações Docker completas para desenvolvimento e produção.

### Produção (PostgreSQL)

```bash
# Construir e executar em produção
make docker-up

# Ou manualmente
docker compose up --build -d
```

### Desenvolvimento (SQLite)

```bash
# Executar em modo desenvolvimento (porta 8001)
make docker-dev-up

# Ou manualmente
docker compose --profile dev up --build -d
```

### Comandos Docker Úteis

```bash
# Ver logs
make docker-logs

# Parar containers
make docker-down          # Produção
make docker-dev-down      # Desenvolvimento

# Construir apenas
make docker-build
```

### Configuração Docker

- **Produção**: PostgreSQL + Gunicorn (porta 8000)
- **Desenvolvimento**: SQLite + Django dev server (porta 8001)
- **Healthchecks**: Verificação automática de saúde dos serviços
- **Volumes**: Persistência de dados PostgreSQL e arquivos estáticos

```bash
# Construir e executar em produção
make docker-up

# Ou manualmente
docker compose up --build -d
```

### Desenvolvimento (SQLite)

```bash
# Executar em modo desenvolvimento (porta 8001)
make docker-dev-up

# Ou manualmente
docker compose --profile dev up --build -d
```

### Comandos Docker Úteis

```bash
# Ver logs
make docker-logs

# Parar containers
make docker-down          # Produção
make docker-dev-down      # Desenvolvimento

# Construir apenas
make docker-build
```

### Configuração Docker

- **Produção**: PostgreSQL + Gunicorn (porta 8000)
- **Desenvolvimento**: SQLite + Django dev server (porta 8001)
- **Healthchecks**: Verificação automática de saúde dos serviços
- **Volumes**: Persistência de dados PostgreSQL e arquivos estáticos

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

## Desenvolvimento

### Configuração Inicial

```bash
# Clonar repositório
git clone <repo-url>
cd dajngo

# Criar ambiente virtual
python -m venv myworld
myworld\Scripts\activate  # Windows

# Instalar dependências
make install

# Configurar banco
make migrate
make createsuperuser

# Executar
make runserver
```

### Com Docker

```bash
# Desenvolvimento rápido
make docker-dev-up

# Produção
make docker-up
```

### Testes

```bash
make test
```

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
- **Banco**: SQLite (dev) / PostgreSQL (prod via Docker)
- **Autenticação**: Sessions (web) + JWT (API)
- **Container**: Docker + Docker Compose (produção + desenvolvimento)
- **Servidor**: Gunicorn (produção) / Django dev server (desenvolvimento)
- **Tema**: Interface dark inspirada em Elden Ring
- **Build**: Otimizado com .dockerignore e multi-stage
- **Tratamento de Erros**: Sistema robusto com fallbacks
- **Templates**: Organizados com herança (base.html)

## Estrutura do Projeto

```
dajngo/
├── core/                          # App principal
│   ├── migrations/               # Migrações do banco
│   ├── templates/core/           # Templates HTML
│   ├── models.py                 # Modelos Django
│   ├── views.py                  # Views e lógica
│   ├── urls.py                   # URLs da aplicação
│   ├── admin.py                  # Configuração admin
│   ├── serializers.py            # Serializers REST (removido)
│   └── eldenring_api.py          # Cliente API Elden Ring
├── eldendemo/                    # Configurações Django
│   ├── settings.py               # Configurações principais
│   ├── urls.py                   # URLs do projeto
│   ├── wsgi.py                   # Configuração WSGI
│   └── asgi.py                   # Configuração ASGI
├── dockerfile                    # Dockerfile otimizado
├── docker-compose.yml            # Configuração Docker
├── .dockerignore                 # Arquivos ignorados no Docker
├── requirements.txt              # Dependências Python
├── Makefile                      # Comandos de automação
├── manage.py                     # Script Django
└── README.md                     # Esta documentação
```