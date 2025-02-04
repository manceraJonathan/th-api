from sqlalchemy.orm import Session
from app.schemas.log import LogCreate
from . import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_log(db: Session, log_data: LogCreate):
    log_entry = models.Log(**log_data.model_dump())
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    return log_entry


def get_log(db: Session, log_id: int):
    return db.query(models.Log).filter(models.Log.id == log_id).first()
