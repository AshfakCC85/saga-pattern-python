from typing import List, Optional

from sqlmodel import SQLModel, create_engine, Session, select
from models import Customer

sqlite_file_name = "database.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

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
        return results