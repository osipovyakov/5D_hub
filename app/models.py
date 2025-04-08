from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from .database import Base


class URLRequest(BaseModel):
    original_url: str


class URLResponse(BaseModel):
    shortened_url: str


class URL(Base):
    __tablename__ = 'shortened_url'
    
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, unique=True, index=True)
    shortened_url = Column(String, unique=True, index=True)
