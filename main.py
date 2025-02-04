from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, database
from app.schemas.log import LogCreate
from pydantic import BaseModel

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/logs/{log_id}")
def read_log(log_id: int, db: Session = Depends(get_db)):
    log = crud.get_log(db=db, log_id=log_id)
    if log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return log


@app.post("/logs/")
def create_log(log_data: LogCreate, db: Session = Depends(get_db)):
    return crud.create_log(db=db, log_data=log_data)
