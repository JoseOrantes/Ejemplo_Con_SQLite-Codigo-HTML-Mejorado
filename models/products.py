import json
import os

PRODUCTS_FILE = os.path.join("data", "products.json")

#Cargando JSON
def loadProducts():
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'r') as file:
            return json.load(file) #Devuelve la lista completa
    return []

def saveProducts(products):
    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ident=4)
        
def getProductById(idProduct):
    products = loadProducts()
    return next((p for p in products if p["id"] == idProduct), None)