from app.models.cart import Cart
from app.models.product import Product
from . import db


class CartProducts(db.Model):
    '''Many to many relationship table for cart and products'''
    __tablename__ = 'cart_products'

    cart_id: int = db.Column(db.ForeignKey('cart.id'), primary_key=True)
    product_id: int = db.Column(db.ForeignKey('product.id'), primary_key=True)
    cart = db.relationship(
        'Cart', back_populates='products')
    product = db.relationship('Product', back_populates='carts')
    product_amount: int = db.Column(db.Integer, nullable=False)

    def __init__(self, cart=None, product=None) -> None:
        if cart is not None:
            self.cart = cart
        if product is not None:
            self.product = product
        self.product_amount = 1
