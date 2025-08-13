#!/bin/sh
set -e

echo "Comprobando conexión a PostgreSQL..."

# Intentar conectar a PostgreSQL
if python -c "import psycopg2; psycopg2.connect(
    dbname='${POSTGRES_DB}',
    user='${POSTGRES_USER}',
    password='${POSTGRES_PASSWORD}',
    host='${POSTGRES_HOST}',
    port='${POSTGRES_PORT}'
)"; then
    export DATABASE_ENGINE="postgresql"
    echo "✅ PostgreSQL disponible. Usando PostgreSQL."
else
    echo "⚠️ No se pudo conectar a PostgreSQL. Cambiando a SQLite."
    export DATABASE_ENGINE="sqlite"
fi

cd ./app/starchips_project

echo "Ejecutando migraciones..."
python manage.py migrate --noinput

echo "Arrancando servidor..."
python manage.py runserver 0.0.0.0:8000
