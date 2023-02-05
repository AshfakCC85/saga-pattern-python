from typing import List

from sqlmodel import SQLModel, create_engine, Session, select
from models import Customer

sqlite_file_name = "database.sqlite"
sqlite_url = "postgresql://customer_db/?user=postgres&password=postgres"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_customers() -> List[Customer]:
    with Session(engine) as session:
        statement = select(Customer)
        results = session.exec(statement)
        results = results.all()
        return results


def get_customer(id) -> Customer:
    with Session(engine) as session:
        statement = select(Customer).where(Customer.id==id)
        results = session.exec(statement)
        results = results.first()
        print('here', results)
        return results


def create_customer(customer):
    with Session(engine) as session:
        db_cus = Customer.from_orm(customer)
        session.add(db_cus)
        session.commit()
        session.refresh(db_cus)
        return db_cus