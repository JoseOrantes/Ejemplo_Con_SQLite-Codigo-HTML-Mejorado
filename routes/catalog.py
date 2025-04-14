from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.products import loadProducts

catalgo_bp = Blueprint("catalog", __name__)

@catalgo_bp.route("/catalog")
def products():
    if "cui" not in session:
        return redirect(url_for("auth.login"))
    
    products = loadProducts()
    return render_template("catalog.html", products=products)

