import asyncio
import random
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Order
from config import DATABASE_URL
from faker import Faker

fake = Faker()

async def seed_db():
    engine = create_async_engine(DATABASE_URL)
    AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with AsyncSessionLocal() as session:
        orders = []
        for _ in range(50):
            order = Order(
                customer_name=fake.name(),
                total_price=round(random.uniform(10.0, 500.0), 2),
                status=random.choice(["new", "processing", "shipped", "delivered"]),
                created_at=fake.date_time_this_year()
            )
            orders.append(order)

        session.add_all(orders)
        await session.commit()
        print(f"Added {len(orders)} orders to the database.")

if __name__ == "__main__":
    asyncio.run(seed_db())