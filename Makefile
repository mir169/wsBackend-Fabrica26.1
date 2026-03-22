# Makefile para o projeto Django EldenDemo

.PHONY: help install migrate makemigrations createsuperuser runserver shell test clean docker-build docker-up docker-down docker-logs docker-dev-up docker-dev-down

help:
	@echo "Comandos disponíveis:"
	@echo "  make install             - Instala dependências no ambiente local (venv)"
	@echo "  make makemigrations      - Cria migrações"
	@echo "  make migrate             - Aplica migrações"
	@echo "  make createsuperuser     - Cria superusuário Django"
	@echo "  make runserver           - Inicia o servidor local"
	@echo "  make shell               - Abre shell Django"
	@echo "  make test                - Executa testes"
	@echo "  make clean               - Remove arquivos temporários"
	@echo "  make docker-build        - Constrói imagem Docker do app"
	@echo "  make docker-up           - Sobe containers produção (PostgreSQL)"
	@echo "  make docker-down         - Para e remove containers produção"
	@echo "  make docker-logs         - Exibe logs do serviço web"
	@echo "  make docker-dev-up       - Sobe containers desenvolvimento (SQLite)"
	@echo "  make docker-dev-down     - Para containers desenvolvimento"

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

test:
	python manage.py test

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .coverage coverage.xml

docker-build:
	docker compose build

docker-up:
	docker compose up -d --build

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f web

docker-dev-up:
	docker compose --profile dev up -d --build

docker-dev-down:
	docker compose --profile dev down