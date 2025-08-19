#!/bin/sh

echo "Esperando a PostgreSQL..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 1
done
echo "PostgreSQL disponible"

echo "Ejecutando migraciones..."
python ./starships_project/manage.py migrate

echo "Listo. Arrancando servidor..."
exec "$@"
