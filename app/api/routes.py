
from fastapi import APIRouter
from app.domain.models import Product
from app.services.product_service import (
    create_product,
    fetch_product,
    fetch_all_products
)

router = APIRouter()

@router.post("/")
def add(product: Product):
    return create_product(product)

@router.get("/")
def get_all():
    return fetch_all_products()

@router.get("/{product_id}")
def get_one(product_id: str):
    return fetch_product(product_id)
