
products_db = {}

def add_product(product):
    products_db[product.id] = product
    return product

def get_product(product_id):
    return products_db.get(product_id)

def list_products():
    return list(products_db.values())
