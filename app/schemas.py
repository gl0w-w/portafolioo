from  pydantic import BaseModel
from typing import Optional

class ProyectoBase(BaseModel):
    titulo: str
    descripcion: str
    imagen_url: str
    enlace: Optional[str] = None

class ProyectoCreate(ProyectoBase):
    pass

class ProyectoResponse(ProyectoBase):
    id: int
    
    class Config:
        from_attibutes = True
        
