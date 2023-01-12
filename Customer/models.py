from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int] = None
    count: int = 100
    created_at: datetime = datetime.now()
    available_credit: float = 1000
    remaining_credit: float = 1000
