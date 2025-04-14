from flask import Flask
from routes.auth import auth_bp
from routes.catalog import catalgo_bp
from routes.cart import cart_bp

app = Flask(__name__)
app.secret_key = 'supersecreto' #Para Flash 

#ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app.register_blueprint(auth_bp)
app.register_blueprint(catalgo_bp)
app.register_blueprint(cart_bp)

@app.context_processor
def injectCartCount():
    from routes.cart import getCartCount
    return { "cartCount": getCartCount() }

if __name__ == '__main__':
    app.run(debug=True)