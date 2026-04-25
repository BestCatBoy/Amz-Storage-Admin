from sqlalchemy.ext.asyncio import AsyncEngine
from starlette_admin.contrib.sqla import Admin, ModelView
from auth import MyAuthProvider
from models import Order

def create_admin(engine: AsyncEngine) -> Admin:
    admin = Admin(engine, title="Admin")
    admin.add_view(ModelView(Order))

    provider = MyAuthProvider()
    provider.setup_admin(admin)

    return admin