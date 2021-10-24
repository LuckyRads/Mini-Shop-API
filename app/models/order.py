from . import db
from datetime import datetime


class Order(db.Model):
    '''Database order model'''
    __tablename__ = 'order'

    id: int = db.Column(db.Integer, primary_key=True)
    created_at: datetime = db.Column(db.DateTime, nullable=False)
    finished_at: datetime = db.Column(db.DateTime)
    is_finished: bool = db.Column(db.Boolean, nullable=False)
    status: str = db.Column(db.String(100))
    total_price: float = db.Column(db.Numeric(10, 2), nullable=False)
    products = db.relationship(
        'OrderProducts', back_populates='order')

    def __init__(self) -> None:
        self.created_at = datetime.now()
        self.status = 'Order placed'
        self.is_finished = False
        self.total_price = 0

    def as_dict(self) -> dict:
        serialized_products = []
        for order_product in self.products:
            serialized_product = order_product.product.as_dict()
            serialized_product['product_amount'] = order_product.product_amount
            serialized_products.append(serialized_product)

        return {'id': self.id, 'created_at': self.created_at,
                'finished_at': self.finished_at,
                'is_finished': self.is_finished,
                'status': self.status,
                'total_price': self.total_price,
                'products': serialized_products}
