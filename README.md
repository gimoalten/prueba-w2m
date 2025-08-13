# prueba-w2m

```bash
docker build -t starships .
docker run -d -p 8000:8000 starships
http://localhost:8000/api/starships/ 
```

```bash
docker compose up --build
http://localhost:8000/api/starships/ 
```


```bash
http://localhost:8000/api/starships/ 
    """
    GET: Lista de naves espaciales (paginada).
    Filtro opcional por parámetro ?q= para buscar en nombre.
    POST: Crear nueva nave.
    """
```

```bash
http://localhost:8000/api/starships/<int:pk>
    """
    GET: Recuperar nave por ID (log si ID negativo).
    PUT/PATCH: Modificar nave.
    DELETE: Eliminar nave.
    """
```