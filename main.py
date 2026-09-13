from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.database import engine, Base
from app.routers import proyectos
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Portafolio")

app.include_router(proyectos.router)

app.mount("/static", StaticFiles(directory="public"), name="static")

templates = Jinja2Templates(directory=".")


@app.get("/", response_class=HTMLResponse)
def leer_inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )
