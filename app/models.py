from sqlalchemy import Column, Integer, String
from app.database import Base


class Proyecto(Base):
    __tablename__ = "proyectos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String)
    imagen_url = Column(String)
    enlace = Column(String, nullable=True)
