from . import handle_request, cart_routes
from flask import request
from app.controllers.cart_controller import CartController


@cart_routes.route('/cart/<id>', methods=['GET'])
def get_cart(id) -> tuple:
    if request.method == 'GET':
        return handle_request(CartController.get_cart, id)


@cart_routes.route('/carts', methods=['GET'])
def get_carts() -> tuple:
    if request.method == 'GET':
        return handle_request(CartController.get_carts, id)


@cart_routes.route('/cart', methods=['POST'])
def create_cart() -> tuple:
    if request.method == 'POST':
        return handle_request(CartController.create_cart, request.json)


@cart_routes.route('/cart', methods=['PUT'])
def add_to_cart() -> tuple:
    if request.method == 'PUT':
        return handle_request(CartController.add_to_cart, request.json)


@cart_routes.route('/cart/<id>/total', methods=['GET'])
def get_cart_total(id) -> tuple:
    if request.method == 'GET':
        return handle_request(CartController.get_cart_total, id)
