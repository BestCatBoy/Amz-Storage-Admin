import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Unit(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    full_name = Column(String(100))

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    reg_number = Column(String(20), unique=True, index=True)
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(Text)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    sku = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    unit_id = Column(Integer, ForeignKey("units.id"))

    unit = relationship("Unit", lazy="joined")

class StockItem(Base):
    __tablename__ = "stock_items"
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("items.id"), unique=True)
    quantity = Column(Float, default=0.0)

    item = relationship("Item", lazy="joined")

class Batch(Base):
    __tablename__ = "batches"
    id = Column(Integer, primary_key=True)
    public_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    status = Column(Integer, default=0)

    customer = relationship("Customer", lazy="joined")
    items = relationship("BatchItem", back_populates="batch")

class BatchItem(Base):
    __tablename__ = "batch_items"
    id = Column(Integer, primary_key=True)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    quantity = Column(Float, nullable=False)

    batch = relationship("Batch", back_populates="items")
    item = relationship("Item", lazy="joined")