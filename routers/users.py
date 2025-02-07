from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import get_user
from app.dependencies import get_db


router = APIRouter()


@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
