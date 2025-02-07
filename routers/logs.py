from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.dependencies import get_db
from app.schemas.log import LogCreate


router = APIRouter()


@router.get("/logs/{log_id}")
def read_log(log_id: int, db: Session = Depends(get_db)):
    log = crud.get_log(db=db, log_id=log_id)
    if log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return log


@router.post("/logs/")
def create_log(log_data: LogCreate, db: Session = Depends(get_db)):
    return crud.create_log(db=db, log_data=log_data)
