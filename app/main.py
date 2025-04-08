from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .models import URLRequest, URLResponse
from .crud import save_url, get_original_url
from .database import init_db, get_db

app = FastAPI()

# Инициализация базы данных при старте
@app.on_event('startup')
def startup():
    init_db()

# Эндпоинт для сокращения URL
@app.post('/', response_model=URLResponse, status_code=201)
async def shorten_url(url_request: URLRequest, db: Session = Depends(get_db)):
    shortened_url = save_url(db, url_request.original_url)

    return URLResponse(shortened_url=shortened_url)

# Эндпоинт для получения полного URL
@app.get('/{shortened_url}', response_class=RedirectResponse, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def redirect_to_original_url(shortened_url: str, db: Session = Depends(get_db)):
    original_url = get_original_url(db, shortened_url)
    if original_url:
        return RedirectResponse(url=original_url)
    raise HTTPException(status_code=404, detail='Сокращённый URL не найден')
