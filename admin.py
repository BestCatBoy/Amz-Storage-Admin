from sqlalchemy.ext.asyncio import AsyncEngine
from starlette_admin.contrib.sqla import Admin, ModelView
from auth import MyAuthProvider
from models import Unit, Customer, Item, StockItem, Batch, BatchItem
from starlette_admin import CollectionField, IntegerField, TextAreaField, StringField
import json
from sqlalchemy.orm import joinedload


class UnitView(ModelView):
    identity = "unit"
    label = "Единицы измерения"

class CustomerView(ModelView):
    identity = "customer"
    label = "Заказчики"

class ItemView(ModelView):
    identity = "item"
    label = "Номенклатура"

    async def find_all(self, request, skip=0, limit=100, where=None, order_by=None):
##        print("\n" + "="*50, flush=True)
##        print(f"URL: {request.url}", flush=True)
##        print(f"METHOD: {request.method}", flush=True)
##        print(f"QUERY PARAMS: {dict(request.query_params)}", flush=True)
##        print("="*50 + "\n", flush=True)
        return await super().find_all(request, skip, limit, where, order_by)


class StockItemView(ModelView):
    identity = "stock_item"
    label = "Остатки на складе"

    async def build_query(self, where, request):
        stmt = await super().build_query(where, request)
        return stmt.options(joinedload(StockItem.item))

class BatchView(ModelView):
    identity = "batch"
    label = "Партии"
    fields = [
        "id",
        StringField("public_id", read_only=True, label="UUID"),
        "customer",
        TextAreaField("items_data", label="Состав партии")
    ]

    exclude_fields_from_create = ["public_id", "status"]

    async def before_create(self, request, data, obj):
        raw_items = data.pop("items_data", "[]") or "[]"
        items_list = json.loads(raw_items) if isinstance(raw_items, str) else raw_items
        obj.items = [
            BatchItem(item_id=int(i['item_id']), quantity=float(i['quantity']))
            for i in items_list
        ]

class BatchItemView(ModelView):
    identity = "batch_item"
    label = "Содержимое партии"

def create_admin(engine: AsyncEngine) -> Admin:
    admin = Admin(engine, title="Панель администрирования", templates_dir="templates")

    admin.add_view(UnitView(Unit))
    admin.add_view(CustomerView(Customer))
    admin.add_view(ItemView(Item))
    admin.add_view(StockItemView(StockItem))
    admin.add_view(BatchView(Batch))
    admin.add_view(BatchItemView(BatchItem))

    provider = MyAuthProvider()
    provider.setup_admin(admin)

    return admin