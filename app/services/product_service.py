
from app.repository.product_repository import (
    add_product,
    get_product,
    list_products
)

def create_product(product):
    return add_product(product)

def fetch_product(product_id):
    return get_product(product_id)

def fetch_all_products():
    return list_products()
