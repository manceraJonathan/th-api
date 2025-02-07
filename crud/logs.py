from sqlalchemy.orm import Session
from app.models import Log
from app.schemas import LogCreate

# logs
def create_log(db: Session, log_data: LogCreate):
    log_entry = Log(**log_data.model_dump())
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    return log_entry


def get_log(db: Session, log_id: int):
    return db.query(Log).filter(Log.id == log_id).first()
