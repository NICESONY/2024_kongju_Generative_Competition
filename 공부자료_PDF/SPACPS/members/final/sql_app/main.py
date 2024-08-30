from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="sql_app/templates")

app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/icon", StaticFiles(directory="icon"), name="icon")
app.mount("/Logo", StaticFiles(directory="Logo"), name="Logo")
app.mount("/illust", StaticFiles(directory="illust"), name="illust")
app.mount("/photo", StaticFiles(directory="photo"), name="photo")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("create_record.html", {"request": request})

@app.post("/records/", response_class=HTMLResponse)
async def create_record(
    request: Request, 
    photo_url: str = Form(''), 
    date: str = Form(...), 
    location: str = Form(...), 
    user_id: str = Form(...), 
    title: str = Form(...), 
    hashtag: str = Form(...), 
    content: str = Form(...), 
    db: Session = Depends(get_db)
):
    record = schemas.RecordCreate(
        photo_url=photo_url, 
        date=date, 
        location=location, 
        user_id=user_id, 
        title=title, 
        hashtag=hashtag, 
        content=content
    )
    crud.create_record(db=db, record=record)
    records = crud.get_records(db=db)

    # main4.py에 출력하기
    with open("sql_app/main4.py", "a", encoding="utf-8") as file:
        file.write("\n# Records Output\n")
        for record in records:
            file.write(f"Date: {record.date}\n")
            file.write(f"Location: {record.location}\n")
            file.write(f"User ID: {record.user_id}\n")
            file.write(f"Title: {record.title}\n")
            file.write(f"Hashtag: {record.hashtag}\n")
            file.write(f"Content: {record.content}\n")
            file.write("------\n")

    return templates.TemplateResponse("records.html", {"request": request, "records": records})

@app.get("/records/", response_class=HTMLResponse)
def read_records(request: Request, db: Session = Depends(get_db)):
    records = crud.get_records(db, skip=0, limit=10)

    # main4.py에 출력하기
    with open("sql_app/main4.py", "a", encoding="utf-8") as file:
        file.write("\n# Records Output\n")
        for record in records:
            file.write(f"Date: {record.date}\n")
            file.write(f"Location: {record.location}\n")
            file.write(f"User ID: {record.user_id}\n")
            file.write(f"Title: {record.title}\n")
            file.write(f"Hashtag: {record.hashtag}\n")
            file.write(f"Content: {record.content}\n")
            file.write("------\n")

    return templates.TemplateResponse("records.html", {"request": request, "records": records})
