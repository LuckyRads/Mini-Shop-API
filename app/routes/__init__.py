from flask import Blueprint
from app.exceptions.exceptions import HttpException

product_routes = Blueprint('product_routes', __name__)
cart_routes = Blueprint('cart_routes', __name__)
order_routes = Blueprint('order_routes', __name__)


def handle_request(func, *args) -> tuple:
    try:
        if len(args) == 0:
            response = func()
        elif len(args) >= 1:
            response = func(*args)
        return (response, 200)
    except HttpException as e:
        return ({'status': 'failed', 'message': e.message}, e.code)
    except Exception as e:
        print(e)
        return ({'status': 'failed',
                 'message': 'Whoops! Something wrong has happened'}, 500)
