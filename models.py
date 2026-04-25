from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    customer_name = Column(String(100))
    total_price = Column(Float)
    status = Column(String(50), default="new")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)