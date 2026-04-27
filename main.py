from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import ORJSONResponse
from config import DATABASE_URL, SECRET_KEY
from admin import create_admin


engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI(default_response_class=ORJSONResponse, debug=True)
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

admin = create_admin(engine)
admin.mount_to(app)