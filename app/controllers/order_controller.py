from itertools import product
from app.exceptions.exceptions import HttpException
from app.models.cart_products import CartProducts
from app.models.order import Order
from app.models.cart import Cart
from app.models import db
from flask import jsonify
from app.models.order_products import OrderProducts
from app.services.validation_service import ValidationService
from datetime import datetime


class OrderController:

    @staticmethod
    def get_order(id: int) -> Order:
        return jsonify(OrderController.get_db_order(id).as_dict())

    @staticmethod
    def get_db_order(id: int) -> Order:
        order = db.session.query(Order).filter_by(
            id=id).first()
        if order is None:
            raise HttpException(400, 'Order not found')

        return order

    @staticmethod
    def get_order_total(id: int) -> float:
        order = OrderController.get_db_order(id)
        return jsonify({'total': order.get_total()})

    @staticmethod
    def place_order(data: dict) -> dict:
        ValidationService.check_validity(data, ['cart_id'])

        cart = db.session.query(Cart).filter_by(id=data['cart_id']).first()
        if cart is None:
            raise HttpException(400, 'Cart not found')

        order = Order()
        for cart_product in cart.products:
            order.products.append(OrderProducts(cart_product=cart_product))

        order.total_price = cart.total_price

        db.session.add(order)
        db.session.commit()

        db.session.delete(cart)
        db.session.commit()

        return {'status': 'success', 'message': 'Order successfully placed'}
