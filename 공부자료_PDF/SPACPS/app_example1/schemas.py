from pydantic import BaseModel

class UploadBase(BaseModel):
    title: str
    description: str

class UploadCreate(UploadBase):
    pass

class Upload(UploadBase):
    id: int
    image_path: str

    class Config:
        orm_mode = True
