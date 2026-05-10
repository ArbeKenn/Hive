# Hive
API для школьной социальной сети

## Стек
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT авторизация

## Endpoints
- `POST /user/reg` — registration
- `POST /user/log` — login
- `GET /user/my_profile` — profile 🔒
- `PUT /user/my_profile/edit` — edit_profile 🔒
- `DEL /user/my_profile/del` — del user 🔒
- 
- `GET /post/posts` — all posts
- `POST /post/new_post` — create post 🔒
- `PUT /post/edit` — edit post 🔒
- `DEL /post/del/{post_id}` — del post 🔒

🔒 — requires JWT token
## Запуск
1. `pip install -r requirements.txt`
2. Создай `.env` файл с `DATABASE_URL` и `SECRET_KEY`
3. `uvicorn app.main:app --reload`