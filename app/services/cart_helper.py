from app.models.cart import Cart
from app.models.cart_products import CartProducts


class CartHelper:
    '''Helper class for various cart related calculations'''

    __free_product_divisor: int = 5
    __same_type_discount_amnt = 1
    __same_type_discount_threshold = 20
    __max_cart_total = 100

    @staticmethod
    def get_total(cart: Cart) -> float:
        total = 0

        for cart_product in cart.products:
            total += CartHelper.get_product_group_price(cart_product)

        total = CartHelper.apply_discount_if_eligible(total)
        return total

    @staticmethod
    def get_product_group_price(cart_product: CartProducts) -> float:
        free_product_amount = cart_product.product_amount // CartHelper.__free_product_divisor
        return (cart_product.product_amount -
                free_product_amount) * cart_product.product.price

    @staticmethod
    def apply_discount_if_eligible(total: float) -> float:
        if (total >= CartHelper.__same_type_discount_threshold):
            return total - CartHelper.__same_type_discount_amnt
        return total

    @staticmethod
    def is_total_exceeding_limit(total: float) -> bool:
        return total > CartHelper.__max_cart_total
