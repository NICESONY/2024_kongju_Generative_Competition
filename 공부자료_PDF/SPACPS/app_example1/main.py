from fastapi import FastAPI
from routes import upload
from database import engine
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(upload.router, prefix="/upload")
