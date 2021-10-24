from datetime import datetime
from . import db


class Cart(db.Model):
    '''Database cart model'''
    __tablename__ = 'cart'

    id: int = db.Column(db.Integer, primary_key=True)
    created_at: datetime = db.Column(db.DateTime)
    total_price: float = db.Column(db.Numeric(10, 2))
    products = db.relationship(
        'CartProducts', back_populates='cart', cascade='delete')

    def __init__(self) -> None:
        self.created_at = datetime.now()

    def as_dict(self) -> dict:
        serialized_products = []
        for cart_product in self.products:
            serialized_product = cart_product.product.as_dict()
            serialized_product['product_amount'] = cart_product.product_amount
            serialized_products.append(serialized_product)

        return {'id': self.id, 'created_at': self.created_at,
                'total_price': self.total_price,
                'products': serialized_products}
