from app.exceptions.exceptions import HttpException
from app.models.cart import Cart
from app.models import db
from flask import jsonify
from app.models.cart_products import CartProducts
from app.models.product import Product
from app.services.cart_helper import CartHelper
from app.services.validation_service import ValidationService


class CartController:

    @staticmethod
    def get_cart(id: int) -> Cart:
        return jsonify(CartController.get_db_cart(id).as_dict())

    @staticmethod
    def get_db_cart(id: int) -> Cart:
        cart = db.session.query(Cart).filter_by(
            id=id).first()
        if cart is None:
            raise HttpException(400, 'Cart not found')

        return cart

    @staticmethod
    def get_carts() -> list:
        carts = db.session.query(Cart).all()
        serialized_carts = []

        for cart in carts:
            serialized_carts.append(cart.as_dict())

        return jsonify(serialized_carts)

    @staticmethod
    def create_cart(data: dict) -> dict:
        ValidationService.check_validity(data, ['product_id'])

        product = db.session.query(Product).filter_by(
            id=data['product_id']).first()
        if (product is None):
            raise HttpException(400, 'Product not found')

        cart = Cart()
        cart.products.append(CartProducts(product=product))
        cart.total_price = CartHelper.get_total(cart)

        if (CartHelper.is_total_exceeding_limit(cart.total_price)):
            raise HttpException(
                400, 'Could not create cart. Maximum cart total was exceeded')

        db.session.add(cart)
        db.session.commit()

        return {'status': 'success', 'message': 'Cart successfully created'}

    @staticmethod
    def add_to_cart(data: dict) -> dict:
        ValidationService.check_validity(data, ['cart_id', 'product_id'])

        cart = db.session.query(Cart).filter_by(id=data['cart_id']).first()
        if (cart is None):
            raise HttpException(400, 'Cart does not exist')

        product = db.session.query(Product).filter_by(
            id=data['product_id']).first()
        if (product is None):
            raise HttpException(400, 'Product does not exist')

        cart_products = db.session.query(CartProducts).filter_by(
            cart=cart, product=product).first()

        if cart_products is None:
            cart.products.append(CartProducts(product=product, cart=cart))
            db.session.add(cart)
        else:
            cart_products.product_amount += 1

        cart.total_price = CartHelper.get_total(cart)
        if (CartHelper.is_total_exceeding_limit(cart.total_price)):
            raise HttpException(
                400, 'Could not add product to cart. Maximum cart total was exceeded')

        db.session.commit()

        return {'status': 'success', 'message': 'Product added to cart successfully'}

    @staticmethod
    def get_cart_total(id: int) -> dict:
        cart = CartController.get_db_cart(id)
        total = CartHelper.get_total(cart)
        return {'total': total}

    @staticmethod
    def remove_cart(id: int) -> dict:
        cart = db.session.query(Cart).filter_by(id=id).first()
        if (cart is None):
            raise HttpException(400, 'Cart does not exist')

        db.session.delete(cart)
        db.session.commit()

        return {'status': 'success', 'message': 'Cart removed successfully'}
