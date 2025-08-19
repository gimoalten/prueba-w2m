# Starships Project

Django project to manage starships data, with setup for local development and GitHub CI/CD.

---

## Technologies

- Python 3.13
- Django 5.2.5
- DRF (Django Rest Framework) 
- drf-spectacular (Swagger)
- PostgreSQL 17
- Docker / Docker Compose
- GitHub Actions (linting and tests)

---

## Installation

```bash
git clone https://github.com/gimoalten/prueba-w2m
cd prueba-w2m

python -m venv .venv
- source .venv/bin/activate  # Linux / macOS
- .venv\Scripts\activate     # Windows
 
pip install -r requirements.txt
```

---

## Running the project locally
Build and start the services:
```bash
docker-compose up -d --build
```

Stop services:
```bash
docker-compose down
```

The app will be available at: http://localhost:8000


---
## API Endpoints

Swagger API docs available at: http://localhost:8000/api/docs/

List / Create Starships
```bash
GET /api/starships/
    Returns a paginated list of starships.
    Optional filter: ?q= to search by name.
    
POST /api/starships/
    Create a new starship.
```
Retrieve / Update / Delete Starship by ID
```bash
GET /api/starships/<pk>/
    Retrieve a starship by ID (logs if ID is negative).
    
PUT / PATCH /api/starships/<pk>/
    Update an existing starship. (logs if ID is negative).
    
DELETE /api/starships/<pk>/
    Delete a starship. (logs if ID is negative).
```

---

## Tests and Linting
### Linting (Pylint with Django)
```bash
pylint starships_project/ --load-plugins pylint_django
```

### Tests
```bash
coverage run --source='.' starships_project/manage.py test starships
coverage report
```

In CI/CD, these run automatically via GitHub Actions.
