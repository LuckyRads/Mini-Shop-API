from . import handle_request, product_routes
from flask import request
from app.controllers.product_controller import ProductController


@product_routes.route('/product/<name>', methods=['GET'])
def get_product(name) -> tuple:
    if request.method == 'GET':
        return handle_request(ProductController.get_product, name)


@product_routes.route('/products', methods=['GET'])
def get_products() -> tuple:
    if request.method == 'GET':
        return handle_request(ProductController.get_products)


@product_routes.route('/product', methods=['POST'])
def create_product() -> tuple:
    if request.method == 'POST':
        return handle_request(ProductController.create_product, request.json)


@product_routes.route('/product', methods=['DELETE'])
def delete_product() -> tuple:
    if request.method == 'DELETE':
        return handle_request(ProductController.delete_product, request.json)
