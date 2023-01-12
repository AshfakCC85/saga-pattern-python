from typing import Union

from fastapi import FastAPI

from db import get_customers, get_customer

app = FastAPI()


@app.get("/customers")
def read_root():
    customers = get_customers()
    return customers


@app.get("/customers/{item_id}")
def read_item(item_id: int):
    customer = get_customer(item_id)
    return customer