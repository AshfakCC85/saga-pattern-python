from typing import Union, List

from fastapi import FastAPI, HTTPException

from db import create_db_and_tables, get_all_products, get_product, create_product
from models import Product

app = FastAPI()


@app.get("/product")
def list_products() -> List[Product]:
    return get_all_products()


@app.get("/product/{prod_id}")
def get_single_product(cus_id: int) -> Product:
    customer = get_product(cus_id)
    if not customer:
        raise HTTPException(status_code=404, detail='Product not found')
    return customer

@app.post('/product/', response_model=Product)
def post_product(product: Product) -> Product:
    item = create_product(product)
    return item

@app.on_event('startup')
def main():
    create_db_and_tables()
