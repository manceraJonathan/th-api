from sqlalchemy.orm import Session
from app.models import User

# users
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()