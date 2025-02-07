from sqlalchemy import Column, Integer, String
from app.database import Base


class TipoCompetencia(Base):
    __tablename__ = "tipos_competencia"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
