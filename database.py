from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

host = os.getenv('DB_HOST')
name = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
pwd = os.getenv('DB_PASSWORD')

engine = create_engine(
    f"mysql+pymysql://{user}:{pwd}@{host}/{name}?charset=utf8mb4"
)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()