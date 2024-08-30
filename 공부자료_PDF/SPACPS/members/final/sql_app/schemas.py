from pydantic import BaseModel

class RecordBase(BaseModel):
    photo_url: str
    date: str
    location: str
    user_id: str
    title: str
    hashtag: str
    content: str

class RecordCreate(RecordBase):
    pass

class Record(RecordBase):
    id: int

    class Config:
        from_attributes = True
