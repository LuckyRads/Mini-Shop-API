import numbers

from app.exceptions.exceptions import HttpException
from app.models import db
from app.models.category import Category
from app.models.product import Product
from app.services.validation_service import ValidationService
from app.types.response_types import BasicResponse, StatusEnum
from flask import jsonify


class ProductController:

    @staticmethod
    def get_product(name: str) -> Product:
        product = db.session.query(Product).filter_by(
            name=name).first()
        if product is None:
            raise HttpException(400, 'Product not found')

        return jsonify(product.as_dict())

    @staticmethod
    def get_products() -> list:
        products = db.session.query(Product).all()
        serialized_products = []

        for product in products:
            serialized_products.append(product.as_dict())

        return jsonify(serialized_products)

    @staticmethod
    def create_product(data: dict) -> dict:
        ValidationService.check_validity(data, ['name', 'price', 'category'])
        if isinstance(data['price'], numbers.Number) is False:
            raise HttpException(400, 'Price must be a number')
        if db.session.query(Product).filter_by(
                name=data['name']).first() is not None:
            raise HttpException(400, 'Product already exists')

        category = db.session.query(Category).filter_by(
            name=data['category']).first()
        if category is None:
            raise HttpException(
                400, f'Category {data["category"]} does not exist')

        product = Product(data['name'], data['price'], category)
        db.session.add(product)
        db.session.commit()
        return BasicResponse.get_dict_res(StatusEnum.SUCCESS,
                                          'Product successfully created')

    @ staticmethod
    def delete_product(data: dict) -> dict:
        ValidationService.check_validity(data, ['name'])

        product = db.session.query(Product).filter_by(
            name=data['name']).first()
        if product is None:
            raise HttpException(400, 'Product not found')

        db.session.delete(product)
        db.session.commit()

        return BasicResponse.get_dict_res(StatusEnum.SUCCESS,
                                          'Product deleted successfully')
