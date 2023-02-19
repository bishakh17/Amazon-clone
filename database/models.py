from sqlalchemy import Column, Integer, String, DateTime, Double, ForeignKey
from db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    lattitude = Column(Double, nullable=False)
    longitude = Column(Double, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, phone = {self.phone}, email={self.email}, password={self.password}, lattitude={self.lattitude}, longitude={self.longitude}, created_at={self.created_at})"


class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    lattitude = Column(Double, nullable=False)
    longitude = Column(Double, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"Supplier(id={self.id}, name={self.name}, phone={self.phone}, email={self.email}, password={self.password}, lattitude={self.lattitude}, longitude={self.longitude}, created_at={self.created_at})"


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, description={self.description})"

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"Order(id={self.id}, user_id={self.user_id}, created_at={self.created_at})"


class PriceStock(Base):
    __tablename__ = "supplier_products"
    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    price = Column(Double, nullable=False)
    stock = Column(Integer, nullable=False)

    def __repr__(self):
        return f"SupplierProduct(id={self.id}, supplier_id={self.supplier_id}, product_id={self.product_id}, price={self.price}, stock={self.stock})"


class OrderQuantity(Base):
    __tablename__ = "order_products"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    def __repr__(self):
        return f"OrderProduct(id={self.id}, order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity})"