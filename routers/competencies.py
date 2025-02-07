from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.dependencies import get_db

router = APIRouter()


@router.get("/competencies")
def read_competencies(db: Session = Depends(get_db)):
    return crud.get_competencies(db=db)


@router.post("/competencies")
def create_competencie(nombre: str, id_competencia: int, db: Session = Depends(get_db)):
    competencie = crud.create_competencie(
        db=db, nombre=nombre, id_competencia=id_competencia
    )
    return competencie
