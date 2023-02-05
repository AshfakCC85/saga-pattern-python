from typing import List

from pydantic import BaseModel



class OrderedProducts(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    sub_total: float


class OrderCreate(BaseModel):
    customer_id: int
    customer_name: str
    order_total : float
    products: List[OrderedProducts]