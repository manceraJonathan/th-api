from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import competencies, logs, users

app = FastAPI()

app.include_router(competencies.router)
app.include_router(logs.router)
app.include_router(users.router)
app.add_middleware(CORSMiddleware, allow_origins=["*"])
