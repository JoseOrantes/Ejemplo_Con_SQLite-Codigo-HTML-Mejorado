from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from models.products import loadProducts
import time

cart_bp = Blueprint("cart", __name__)

def getCart():
    # Obetiendo carrito o crea uno nuevo
    return session.get("cart", {})

def saveCart(cart):
    # Guarda carrito en la sesion
    session["cart"] = cart
    session.modified = True

# Agregando producto al carrito
@cart_bp.route("/add/<int:productId>", methods=["POST"])
def addToCart(productId):
    cart = getCart()
    # Cargando productos de json
    products = loadProducts()  
    
    product = next((p for p in products if p["id"] == productId))
    if not product:
        return jsonify({ "Error": "Producto no encontrado" }), 404
    
    # cart: ( "productId": " "1", "cantidad": 2)
    if str(productId) in cart:
        # Agregar repetido
        cart[str(productId)]["quantity"] += 1
    else:
        # Agrega nuevo
        cart[str(productId)] = {
            "name": product["name"],
            "price": product["price"],
            "quantity": 1,
            "picture": product["picture"],
        }
    saveCart(cart)
    return redirect(url_for("catalog.products"))

def getCartCount():
    cart = getCart()
    count = sum(item["quantity"] for item in cart.values())
    return count


# Blueprint para ver el carrito
@cart_bp.route("/cart")
def viewCart():
    cart = getCart()
    total = sum(item['price'] * item["quantity"] for item in cart.values()) 
    cartCount = getCartCount()
    return render_template("cart.html", cart=cart, total=total, cartCount=cartCount)

@cart_bp.route("/remove/<int:productId>", methods=["POST"])
def removeFromCart(productId):
    cart = getCart()
    if str(productId) in cart:
        if cart[str(productId)]["quantity"] > 1:
            cart[str(productId)]["quantity"] -= 1
        else:
            del cart[str(productId)]
        saveCart(cart)
    return redirect(url_for("cart.viewCart"))

#Vaciando el carrito luego de compra
@cart_bp.route("/complete_payment", methods=["POST"])
def completePayment():
    session.pop("cart", None)
    session.modified = True
    flash("Pago completado.")
    time.sleep(3)
    return redirect(url_for("catalog.products"))
