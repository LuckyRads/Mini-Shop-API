from . import handle_request, order_routes
from flask import request
from app.controllers.order_controller import OrderController


@order_routes.route('/order/<id>', methods=['GET'])
def get_order(id) -> tuple:
    if request.method == 'GET':
        return handle_request(OrderController.get_order, id)


@order_routes.route('/order/total/<id>', methods=['GET'])
def get_order_total(id) -> tuple:
    if request.method == 'GET':
        return handle_request(OrderController.get_order_total, id)


@order_routes.route('/order', methods=['POST'])
def place_order() -> tuple:
    if request.method == 'POST':
        return handle_request(OrderController.place_order, request.json)
