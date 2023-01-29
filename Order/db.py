from typing import List

from sqlmodel import SQLModel, create_engine, Session, select
from fastapi import HTTPException

from models import Order, OrderedProducts

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
        order = results.first()
        if not order:
            raise HTTPException(status_code=404, detail={'Error': 'Order not found'})
        st = select(OrderedProducts).where(OrderedProducts.order_id==order.id)
        products = session.exec(st).all()
        return order, products


def create_order_products(products, order_id):
    with Session(engine) as session:
        for product in products:
            st = OrderedProducts.from_orm(product, update={'order_id': order_id})
            session.add(st)
        session.commit()
        st = select(OrderedProducts).where(OrderedProducts.order_id==order_id)
        results = session.exec(st).all()
        return results
