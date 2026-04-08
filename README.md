# Proyecto-DS-2026-1 — Seguridad y autenticación

Trabajo de **desarrollo de software** con enfoque en **seguridad**, **métodos de autenticación** y **autorización** (por ejemplo: contraseñas seguras, JWT, OAuth2, roles y permisos).

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/) (plugin `docker compose` v2)

## Puesta en marcha con Docker

1. Clonar el repositorio y entrar al directorio del proyecto.

2. (Opcional) Crear un archivo `.env` a partir del ejemplo:

   ```bash
   cp .env.example .env
   ```

   Edita `.env` si quieres cambiar usuario/contraseña de PostgreSQL, puerto de la API o la clave secreta para JWT.

3. Levantar servicios (API + PostgreSQL):

   ```bash
   docker compose up --build
   ```

4. Probar:

   - API: [http://localhost:8000](http://localhost:8000)
   - Documentación interactiva (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)
   - Salud: [http://localhost:8000/health](http://localhost:8000/health)

La carpeta del proyecto se monta en el contenedor con **recarga automática** (`--reload`): los cambios en el código se reflejan sin reconstruir la imagen.

## Desarrollo local sin Docker (opcional)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Necesitarás una base PostgreSQL accesible y la variable `DATABASE_URL` si conectas desde el código.

## Contenido del entorno

| Archivo / carpeta | Descripción |
|-------------------|-------------|
| `Dockerfile` | Imagen Python 3.12 con dependencias del proyecto |
| `docker-compose.yml` | Servicios `app` (FastAPI) y `db` (PostgreSQL 16) |
| `requirements.txt` | Dependencias de producción (FastAPI, JWT, SQLAlchemy, etc.) |
| `requirements-dev.txt` | Herramientas de desarrollo (pytest, ruff, mypy) |
| `app/main.py` | Punto de entrada mínimo de la API |

## Próximos pasos sugeridos (curso)

- Modelar usuarios y roles en la base de datos (Alembic para migraciones).
- Implementar registro/login con hash de contraseñas (`passlib` / bcrypt).
- Emitir y validar **JWT**; endpoints protegidos con dependencias FastAPI.
- Explorar **OAuth2** (flujo password o autorización) según lo pida el curso.
- Tests con `pytest` y revisión estática con `ruff` / `mypy`.

## Licencia

Define la licencia de tu curso o institución en este apartado.
