from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import URL
import hashlib

# Генерация короткого URL
def generate_shortened_url(original_url: str) -> str:
    return hashlib.md5(original_url.encode()).hexdigest()[:6]

# Сохранение URL в базе данных
def save_url(db: Session, original_url: str) -> str:
    existing_url = db.query(URL).filter(URL.original_url == original_url).first()
    if existing_url:
        raise HTTPException(status_code=400, detail='Этот URL уже был сокращен')

    shortened_url = generate_shortened_url(original_url)
    db_url = URL(original_url=original_url, shortened_url=shortened_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return shortened_url

# Получение оригинального URL по сокращенному
def get_original_url(db: Session, shortened_url: str) -> str:
    db_url = db.query(URL).filter(URL.shortened_url == shortened_url).first()
    if db_url:
        return db_url.original_url
    return None
