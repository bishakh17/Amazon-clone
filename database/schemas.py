from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class Supplier(BaseModel):
    name: str
    phone: str 
    email: str
    password: str
    lattitude: float
    longitude: float
    created_at: datetime

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
    
