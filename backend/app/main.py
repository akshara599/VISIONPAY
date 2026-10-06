from fastapi import FastAPI
from sqlalchemy import text

from .database import engine

app = FastAPI(title="VISIONPAY API")


@app.get("/")
def root():
    return {"message": "VISIONPAY Backend is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/health/db")
def database_health():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        return {
            "database": "connected",
            "result": result.scalar()
        }
    