import os
from fastapi import APIRouter, Depends, File, UploadFile, Form
from sqlalchemy.orm import Session
import sys 
sys.path.append("/root/naver")
from app import crud, models, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Upload)
async def create_upload(
    title: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_location = f"app/static/images/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    
    upload = schemas.UploadCreate(title=title, description=description)
    return crud.create_upload(db=db, upload=upload, image_path=file_location)
