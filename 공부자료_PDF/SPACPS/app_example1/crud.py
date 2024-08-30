from sqlalchemy.orm import Session
import models, schemas

def create_upload(db: Session, upload: schemas.UploadCreate, image_path: str):
    db_upload = models.Upload(**upload.dict(), image_path=image_path)
    db.add(db_upload)
    db.commit()
    db.refresh(db_upload)
    return db_upload
