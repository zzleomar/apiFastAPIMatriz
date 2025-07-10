FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Exponer puerto por defecto (Railway lo sobrescribirá)
EXPOSE 8000

# Usar sh -c para permitir expansión de variables de entorno
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]