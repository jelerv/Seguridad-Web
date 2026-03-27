FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar requirements primero
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación segura
COPY app.py .

# Exponer el puerto
EXPOSE 5000

# Ejecutar en modo producción (debug desactivado por seguridad)
CMD ["python", "app.py"]
