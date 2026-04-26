# FastAPI Admin Test Project


> ⚠️ **Важно для использования из РФ:**
> Starlette-Admin загружает стили из зарубежных источников, для корректной работы из РФ требуется VPN / прокси

 
## ⚡️ Быстрый старт
1.  **Запуск приложения и базы данных:**
    ```bash
    docker compose up --build -d
    ```
2.  **Проведение миграций:**
    ```bash
    docker-compose exec app alembic upgrade head
    ```
3.  **Доступ к админ-панели:**
    [http://localhost:8000/admin](http://localhost:8000/admin)
