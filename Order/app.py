from typing import Union, List

from fastapi import FastAPI, HTTPException

from db import create_db_and_tables, create_order, get_one_order
from models import Order
from schema import OrderCreate

app = FastAPI()


@app.post('/order/', response_model=Order)
def post_order(order: OrderCreate) -> Order:
    item = create_order(order)
    return item


@app.get('/order/{oid}', response_model=OrderCreate)
def get_order(oid):
    item = get_one_order(oid)
    return item.dict()


@app.on_event('startup')
def main():
    create_db_and_tables()
