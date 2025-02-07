from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Competencies(Base):
    __tablename__ = "competencias"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255), nullable=True)
    tipo_competencia_id = Column(
        Integer, ForeignKey("tipos_competencia.id"), nullable=False
    )
    estado = Column(Boolean, nullable=False)
    fecha_creacion = Column(DateTime, nullable=False)
    tipo_competencia = relationship("TipoCompetencia", backref="competencias")
