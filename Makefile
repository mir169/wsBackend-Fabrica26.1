# Makefile para o projeto Django EldenDemo

.PHONY: help install migrate makemigrations createsuperuser runserver docker-build docker-up docker-down docker-logs shell

help:
	@echo "Comandos disponíveis:"
	@echo "  make install             - Instala dependências no ambiente local (venv)"
	@echo "  make makemigrations      - Cria migrações"
	@echo "  make migrate             - Aplica migrações"
	@echo "  make createsuperuser     - Cria superusuário Django"
	@echo "  make runserver           - Inicia o servidor local"
	@echo "  make shell               - Abre shell Django"
	@echo "  make docker-build        - Constrói imagem Docker do app"
	@echo "  make docker-up           - Sobe containers via docker-compose"
	@echo "  make docker-down         - Para e remove containers"
	@echo "  make docker-logs         - Exibe logs do serviço web"

install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

runserver:
	python manage.py runserver

shell:
	python manage.py shell

docker-build:
	docker compose build

docker-up:
	docker compose up -d --build

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f web