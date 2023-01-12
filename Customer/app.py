from typing import Union

from fastapi import FastAPI

from db import create_db_and_tables

app = FastAPI()


@app.get("/get_customers")
def read_root():
    return {"Hello": "World"}



def main():
    create_db_and_tables()


if __name__ == "__main__":
    main()