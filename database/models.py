import sqlalchemy as sql
from database import Base


class User(Base):
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    name = sql.Column(sql.String(50), nullable=False)
    phone = sql.Column(sql.String(50), nullable=False)
    email = sql.Column(sql.String(50), unique=True, index=True , nullable=False)
    password = sql.Column(sql.String(50), nullable=False)
    lattitude = sql.Column(sql.Double, nullable=False)
    longitude = sql.Column(sql.Double, nullable=False)
    created_at = sql.Column(sql.DateTime, nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, phone = {self.phone}, email={self.email}, password={self.password}, lattitude={self.lattitude}, longitude={self.longitude}, created_at={self.created_at})"

class Supplier(Base):
    __tablename__ = "suppliers"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    name = sql.Column(sql.String(50), nullable=False)
    phone = sql.Column(sql.String(50), nullable=False)
    email = sql.Column(sql.String(50), unique=True, index=True , nullable=False)
    password = sql.Column(sql.String(50), nullable=False)
    lattitude = sql.Column(sql.Double, nullable=False)
    longitude = sql.Column(sql.Double, nullable=False)
    created_at = sql.Column(sql.DateTime, nullable=False)

    def __repr__(self):
        return f"Supplier(id={self.id}, name={self.name}, phone={self.phone}, email={self.email}, password={self.password}, lattitude={self.lattitude}, longitude={self.longitude}, created_at={self.created_at})"


class Product(Base):
    __tablename__ = "products"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    name = sql.Column(sql.String(50), nullable=False)
    description = sql.Column(sql.String(50), nullable=False)

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, description={self.description})"


class Order(Base):
    __tablename__ = "orders"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"), nullable=False)
    created_at = sql.Column(sql.DateTime, nullable=False)

    def __repr__(self):
        return f"Order(id={self.id}, user_id={self.user_id}, created_at={self.created_at})"


class PriceStock(Base):
    __tablename__ = "supplier_products"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    supplier_id = sql.Column(sql.Integer, sql.ForeignKey("suppliers.id"), nullable=False)
    product_id = sql.Column(sql.Integer, sql.ForeignKey("products.id"), nullable=False)
    price = sql.Column(sql.Integer, nullable=False)
    stock = sql.Column(sql.Integer, nullable=False)

    def __repr__(self):
        return f"PriceStock(id={self.id}, supplier_id={self.supplier_id}, product_id={self.product_id}, price={self.price}, stock={self.stock})"


class OrderDetails(Base):
    __tablename__ = "order_products"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    order_id = sql.Column(sql.Integer, sql.ForeignKey("orders.id"), nullable=False)
    product_id = sql.Column(sql.Integer, sql.ForeignKey("products.id"), nullable=False)
    Supplier_id = sql.Column(sql.Integer, sql.ForeignKey("suppliers.id"), nullable=False)
    quantity = sql.Column(sql.Integer, nullable=False)

    def __repr__(self):
        return f"OrderDetails(id={self.id}, order_id={self.order_id}, product_id={self.product_id}, supplier_id={self.supplier_id}, quantity={self.quantity})"