FROM python:3.13-slim

# evitar que python genere archivos .pyc 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# instalar pipenv en el contenedor
RUN pip install --no-cache-dir pipenv

# copiar los archivos de dependencias
COPY Pipfile Pipfile.lock ./

# instalar dependencias del sistema
# --system: instala los paquetes en el Python del sistema (no crea un venv dentro del contenedor)
# --deploy: falla si el Pipfile.lock esta desactualizado
RUN pipenv install --system --deploy

# resto del codigo
COPY . .

CMD ["python", "run.py"]