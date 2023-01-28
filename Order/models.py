from typing import Optional

from sqlmodel import Field, SQLModel

from enums import Status


class OrderedProducts(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int
    product_name: str
    quantity: int
    sub_total: float
    order_id: Optional[int] = Field(default=None, foreign_key="order.id")


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int
    customer_name: str
    order_total : float
    order_status : int = Status.created.value