from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/proyectos",
    tags=["Proyectos"]
)

@router.get("/")
def leer_proyectos():
    pass 

@router.post("/")
def crear_proyecto():
    pass 

@router.put("/{proyecto_id}")
def actualizar_proyecto(proyecto_id: int):
    pass 

@router.delete("/{proyecto_id}")
def eliminar_proyecto(proyecto_id: int):
    pass 