from fastapi import FastAPI
from app.database import engine, Base
from app.routers import proyectos
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Portafolio")

app.include_router(proyectos.router)

@app.get("/")
def read_root():
    return {"mensaje": "api conectada y funcionando"}