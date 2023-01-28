from typing import List

from sqlmodel import SQLModel, create_engine, Session, select
from models import Order

sqlite_file_name = "database.sqlite"
sqlite_url = f"postgresql://order_db/?user=postgres&password=postgres"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_order(order: Order):
    with Session(engine) as session:
        db_cus = Order.from_orm(order)
        session.add(db_cus)
        session.commit()
        session.refresh(db_cus)
        return db_cus


def get_one_order(id) -> Order:
    with Session(engine) as session:
        statement = select(Order).where(Order.id==id)
        results = session.exec(statement)
        results = results.first()
        return results