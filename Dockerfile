# Dockerfile
FROM python:3.10-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt .
COPY app/ ./app/
COPY config/ ./config/
COPY data/ ./data/

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto de la aplicación
EXPOSE 7860

# Comando para ejecutar la app
CMD ["python", "app/main.py"]