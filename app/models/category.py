from . import db


class Category(db.Model):
    '''Database category model'''
    __tablename__ = 'category'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), unique=True)
    products = db.relationship('Product', back_populates='category', lazy=True)

    def __init__(self, name: str) -> None:
        self.name = name

    def as_dict(self) -> dict:
        return {'id': self.id, 'name': self.name}
