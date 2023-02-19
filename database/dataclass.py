from pydantic import BaseModel

class User(BaseModel):
    name: str
    phone: str 
    email: str
    password: str
    lattitude: float
    longitude: float
    created_at: str

class Supplier(BaseModel):
    name: str
    phone: str 
    email: str
    password: str
    lattitude: float
    longitude: float
    created_at: str

class Product(BaseModel):
    name: str
    description: str


class Order(BaseModel):
    user_id: int
    created_at: str 


class PriceStock(BaseModel):
    supplier_id: int
    product_id: int
    price: float
    stock: int

class OrderQuantity(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    
