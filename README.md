# Hive
API для школьной социальной сети

## Стек
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT авторизация

## Endpoints
- `GET /` — home
- 
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

🔒 — требует JWT токен
 
---
 
## 🛠 Установка и запуск
 
### 1. Клонировать репозиторий
```
git clone https://github.com/ArbeKenn/Hive.git
cd Hive
```
 
### 2. Создать виртуальное окружение
```
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```
 
### 3. Установить зависимости
```
pip install -r requirements.txt
```
 
### 4. Настроить переменные окружения
 
Создай файл `.env` в корне проекта:
```
DATABASE_URL=your_database
SECRET_KEY=your_secret_key
```
 
### 5. Запустить приложение
```
uvicorn app.main:app --reload
```
 
После запуска открой в браузере:  
Swagger UI: http://localhost:8000/docs
 
---
 
## 📁 Структура проекта
 
```
Hive/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI приложение
│   ├── database.py       # Подключение к БД
│   ├── user/
│   │   ├── models.py     # SQLAlchemy модель User
│   │   ├── schemas.py    # Pydantic схемы
│   │   ├── router.py     # Эндпоинты пользователей
│   │   └── jwt.py        # JWT логика
│   ├── posts/
│   │   ├── models.py     # SQLAlchemy модель Post
│   │   ├── schemas.py    # Pydantic схемы
│   │   └── router.py     # Эндпоинты публикаций
│   ├── coins/            # В разработке
│   └── violations/       # В разработке
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
 
---
 
## 📝 Что планируется
 
- [ ] Комментарии к постам
- [ ] Система лайков
- [ ] Система коинов для лучших учеников
- [ ] Объявления и новости школы
- [ ] Нарушения дисциплины
- [ ] Alembic миграции
- [ ] Docker
---
 
## 👤 Автор
 
Bektemir – [GitHub](https://github.com/ArbeKenn) – [Telegram](https://t.me/ArbeKenn) – [Email](mailto:bektemir1102@gmail.com)