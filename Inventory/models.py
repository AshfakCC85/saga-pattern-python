from typing import Optional
from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: Optional[int] = None
    brand: str
    stock_available: int = 50
    available_status: bool = True
