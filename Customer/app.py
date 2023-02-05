from typing import List

from fastapi import FastAPI, HTTPException

from db import create_db_and_tables, get_customers, get_customer, create_customer
from models import Customer

app = FastAPI()


@app.get("/customer")
def read_root() -> List[Customer]:
    return get_customers()


@app.get("/customer/{cus_id}")
def read_root(cus_id: int) -> Customer:
    customer = get_customer(cus_id)
    if not customer:
        raise HTTPException(status_code=404, detail='Customer not found')
    return customer

@app.post('/customer/', response_model=Customer)
def post_customer(customer: Customer) -> Customer:
    item = create_customer(customer)
    return item

@app.on_event('startup')
def main():
    create_db_and_tables()
