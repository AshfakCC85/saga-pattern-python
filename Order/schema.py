from typing import List

from models import SQLModel

from enums import Status


class OrderedProducts(SQLModel):
    product_id: int
    product_name: str
    quantity: int
    sub_total: float


class OrderCreate(SQLModel):
    customer_id: int
    customer_name: str
    order_total : float
    products: List[OrderedProducts]