from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    usuario = Column(String)


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, nullable=False)
    usuario_destino_id = Column(Integer, nullable=True)
    nombre_archivo = Column(String(255), nullable=False)
    ruta_archivo = Column(String(255), nullable=False)
    accion = Column(Integer, nullable=False)
    modulo = Column(Integer, nullable=False)
