from fastapi import FastAPI
from indb import generate_products

app = FastAPI()

products = generate_products()

@app.get("/")
async def get_products():
    return {"products": products}