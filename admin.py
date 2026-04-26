from sqlalchemy.ext.asyncio import AsyncEngine
from starlette_admin.contrib.sqla import Admin, ModelView
from auth import MyAuthProvider
from models import Unit, Customer, Nomenclature, Storage, Batch, BatchItem


class UnitView(ModelView):
    identity = "unit"
    label = "Единицы измерения"

class CustomerView(ModelView):
    identity = "customer"
    label = "Заказчики"

class NomenclatureView(ModelView):
    identity = "nomenclature"
    label = "Номенклатура"

class StorageView(ModelView):
    identity = "storage"
    label = "Склад"

class BatchView(ModelView):
    identity = "batch"
    label = "Партии"

class BatchItemView(ModelView):
    identity = "batch_item"
    label = "Содержимое партии"

def create_admin(engine: AsyncEngine) -> Admin:
    admin = Admin(engine, title="Панель администрирования")

    admin.add_view(UnitView(Unit))
    admin.add_view(CustomerView(Customer))
    admin.add_view(NomenclatureView(Nomenclature))
    admin.add_view(StorageView(Storage))
    admin.add_view(BatchView(Batch))
    admin.add_view(BatchItemView(BatchItem))

    provider = MyAuthProvider()
    provider.setup_admin(admin)
    return admin

    return admin
