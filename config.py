import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/my_db")
SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key-change-me")