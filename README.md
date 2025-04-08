# Сервис сокращения URL

HTTP-сервис для сокращения URL-адресов и их последующего восстановления. Написан на FastAPI с использованием SQLite

---

## Возможности

- Сокращение URL (`POST /`)
- Получение оригинального URL по идентификатору (`GET /{shortened_url}`)
- Асинхронная работа сервиса
- Хранение данных в базе (SQLite)

---

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/osipovyakov/url-shortener.git
cd url-shortener
```

### 2. Создать и активировать виртуальное окружение
Сервис написан на Python версии 3.11
```bash
py -3.11 -m venv venv
source venv/Scripts/activate
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Запустить приложение
```bash
uvicorn app.main:app --reload
```

Сервер будет доступен по адресу:
http://127.0.0.1:8000/docs

## Автор
Осипов Яков
GitHub: osipovyakov