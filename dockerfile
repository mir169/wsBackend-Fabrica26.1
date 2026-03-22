# Dockerfile para o projeto Django EldenDemo

FROM python:3.12-slim

# Evitar warnings do Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Coletar arquivos estáticos (opcional para desenvolvimento)
RUN python manage.py collectstatic --noinput --clear || true

# Expor porta
EXPOSE 8000

# Comando para executar
CMD ["gunicorn", "eldendemo.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]