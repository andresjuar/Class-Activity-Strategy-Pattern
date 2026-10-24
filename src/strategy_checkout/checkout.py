from .models import Order
from .behaviors import ShippingCostStrategy

class Checkout:
    def __init__(self, shipping: ShippingCostStrategy) -> None:
        self.shipping = shipping
 
    def shipping_cost(self, order: Order) -> float:
        return self.shipping.calculate(order)
 
    def total(self, order: Order) -> float:
        return order.subtotal + self.shipping_cost(order)