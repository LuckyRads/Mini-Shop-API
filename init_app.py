from app.routes.product_routes import product_routes
from app.routes.cart_routes import cart_routes
from app.routes.order_routes import order_routes
from app.models.product import Product
from app.models.category import Category
from app.models.cart import Cart
from app.models.cart_products import CartProducts
from app.models.order import Order
from app.models.order_products import OrderProducts
from flask import Flask
from app.models import db
from config import DBConfig

app = Flask(__name__)

# DB configuration
app.config['SQLALCHEMY_DATABASE_URI'] = DBConfig.get_mysql_config_string()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)

# Register route blueprints
app.register_blueprint(product_routes)
app.register_blueprint(cart_routes)
app.register_blueprint(order_routes)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
