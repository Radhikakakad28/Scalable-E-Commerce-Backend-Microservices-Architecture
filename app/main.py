from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Product Service")


# Home Route
@app.get("/")
def home():
    return {
        "service": "Product Service Running"
    }


# Product Routes
app.include_router(router, prefix="/products")