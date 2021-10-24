from . import db


class Product(db.Model):
    '''Database product model'''
    __tablename__ = 'product'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), unique=True)
    price: float = db.Column(db.Numeric(10, 2), nullable=False)
    category_id: int = db.Column(
        db.Integer, db.ForeignKey('category.id'), nullable=True)
    category = db.relationship('Category', back_populates='products')
    carts = db.relationship(
        'CartProducts', back_populates='product', cascade='delete')
    orders = db.relationship('OrderProducts', back_populates='product')

    def __init__(self, name: str, price: float, category) -> None:
        self.name = name
        self.price = price
        self.category = category

    def as_dict(self) -> dict:
        return {'id': self.id, 'name': self.name, 'price': self.price,
                'category': self.category.as_dict()}
