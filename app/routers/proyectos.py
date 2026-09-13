from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/api/v1/proyectos", tags=["Proyectos"])


# SELECT - Leer todos los proyectos
@router.get("/", response_model=List[schemas.ProyectoResponse])
def leer_proyectos(db: Session = Depends(get_db)):
    proyectos = db.query(models.Proyecto).all()
    return proyectos


# INSERT - Crear un nuevo proyecto
@router.post("/", response_model=schemas.ProyectoResponse)
def crear_proyecto(proyecto: schemas.ProyectoCreate, db: Session = Depends(get_db)):
    nuevo_proyecto = models.Proyecto(**proyecto.model_dump())
    db.add(nuevo_proyecto)
    db.commit()
    db.refresh(nuevo_proyecto)
    return nuevo_proyecto


# UPDATE - Actualizar un proyecto existente
@router.put("/{proyecto_id}", response_model=schemas.ProyectoResponse)
def actualizar_proyecto(
    proyecto_id: int,
    proyecto_actualizado: schemas.ProyectoCreate,
    db: Session = Depends(get_db),
):
    proyecto = (
        db.query(models.Proyecto).filter(models.Proyecto.id == proyecto_id).first()
    )
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    # Actualiza cada campo con los datos nuevos
    for key, value in proyecto_actualizado.model_dump().items():
        setattr(proyecto, key, value)

    db.commit()
    db.refresh(proyecto)
    return proyecto


# DELETE - Eliminar un proyecto
@router.delete("/{proyecto_id}")
def eliminar_proyecto(proyecto_id: int, db: Session = Depends(get_db)):
    proyecto = (
        db.query(models.Proyecto).filter(models.Proyecto.id == proyecto_id).first()
    )
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    db.delete(proyecto)
    db.commit()
    return {"mensaje": "Proyecto eliminado exitosamente"}
