# Dockerfile for a Flask app (expects requirements.txt and a WSGI callable `app`)
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# system deps (needed for many DB drivers like psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# create non-root user
RUN adduser --disabled-password --gecos "" app \
 && chown -R app:app /app

USER app

EXPOSE 5000

CMD ["python","main.py"]