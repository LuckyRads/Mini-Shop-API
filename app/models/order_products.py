from . import db


class OrderProducts(db.Model):
    '''Many to many relationship table for orders and products'''
    __tablename__ = 'order_products'

    order_id: int = db.Column(db.ForeignKey('order.id'), primary_key=True)
    product_id: int = db.Column(db.ForeignKey('product.id'), primary_key=True)
    order = db.relationship('Order', back_populates='products')
    product = db.relationship('Product', back_populates='orders')
    product_amount: int = db.Column(db.Integer, nullable=False)

    def __init__(self, order=None, cart_product=None) -> None:
        if order is not None:
            self.order = order
        if cart_product is not None:
            self.product = cart_product.product
            self.product_amount = cart_product.product_amount
