from sqlalchemy.orm import Session
from app.models import Competencies, TipoCompetencia

# Competencies
def get_competencies(db: Session):
    result = (
        db.query(
            Competencies.id,
            Competencies.nombre,
            TipoCompetencia.nombre.label("tipo_competencia_nombre"),
        )
        .join(
            TipoCompetencia,
            Competencies.tipo_competencia_id == TipoCompetencia.id,
        )
        .all()
    )
    return [
        {"id": r.id, "nombre": r.nombre, "tipo_competencia": r.tipo_competencia_nombre}
        for r in result
    ]


def create_competencie(db: Session, nombre: str, id_competencia: int):
    competencie = Competencies(nombre=nombre, tipo_competencia_id=id_competencia)
    db.add(competencie)
    db.commit()
    db.refresh(competencie)
    return competencie