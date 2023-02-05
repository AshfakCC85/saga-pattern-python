from typing import List

from sqlmodel import SQLModel, create_engine, Session, select
from models import Product

sqlite_file_name = "database.sqlite"
sqlite_url = "postgresql://product_db/?user=postgres&password=postgres"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_all_products() -> List[Product]:
    with Session(engine) as session:
        statement = select(Product)
        results = session.exec(statement)
        results = results.all()
        return results


def get_product(id) -> Product:
    with Session(engine) as session:
        statement = select(Product).where(Product.id==id)
        results = session.exec(statement)
        results = results.first()
        return results


def create_product(product: Product):
    with Session(engine) as session:
        db_cus = Product.from_orm(product)
        session.add(db_cus)
        session.commit()
        session.refresh(db_cus)
        return db_cus