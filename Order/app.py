from typing import Union, List

from fastapi import FastAPI, HTTPException

from db import create_db_and_tables, create_order, get_one_order, create_order_products
from models import Order
from schema import OrderCreate

app = FastAPI()


@app.post('/order/', response_model=OrderCreate)
def post_order(order: OrderCreate) -> Order:
    products = order.products
    item = create_order(order)
    product_in_db = create_order_products(products, order_id=item.id)
    return OrderCreate(**item.dict(), products=product_in_db)


@app.get('/order/{order_id}', response_model=OrderCreate)
def get_order(order_id):
    order, products = get_one_order(order_id)
    return OrderCreate(**order.dict(), products=products)


@app.on_event('startup')
def main():
    create_db_and_tables()
