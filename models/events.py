from typing import Optional, List
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Column, JSON


class Event(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  title: str
  image: str
  description: str
  tags: List[str] = Field(sa_column=Column(JSON))
  location: str

  class Config:
    arbitrary_types_allowed = True

    json_schema_extra = {
        "example": {
            "title": "FastAPI BookLaunch",
            "image": "https://linktomyimage.com/image.png",
            "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
            "tags": ["python", "fastapi", "book", "launch"],
            "location": "Google Meet"
        }
    }


class EventUpdate(SQLModel):
  title: Optional[str] = None
  image: Optional[str] = None
  description: Optional[str] = None
  tags: Optional[List[str]] = None
  location: Optional[str] = None

  class Config:
    json_schema_extra = {
        "example": {
            "title": "FastAPI BookLaunch",
            "image": "https://linktomyimage.com/image.png",
            "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
            "tags": ["python", "fastapi", "book", "launch"],
            "location": "Google Meet"
        }
    }
