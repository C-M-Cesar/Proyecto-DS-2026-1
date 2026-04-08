"""
API base del curso: seguridad, autenticación y autorización.
Amplía este módulo con rutas protegidas, JWT, roles, etc.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Curso DS — Autenticación y autorización",
    description="Proyecto de desarrollo de software enfocado en seguridad.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "API en ejecución. Documentación: /docs",
        "docs": "/docs",
    }
