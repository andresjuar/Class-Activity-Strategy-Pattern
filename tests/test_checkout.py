from strategy_checkout.behaviors import (
    ExpressShipping,
    PickupShipping,
    SameDayShipping,
    StandardShipping,
    ShippingCostStrategy
)

from strategy_checkout.checkout import Checkout
from strategy_checkout.models import Order

class ExampleShipping(ShippingCostStrategy):
    """ Prueba de que checkout funciona con una clase de shipping nuevo """
    def calculate(self, order: Order) -> float:
        return 10.0

def test_standard_shipping_costs_49_below_threshold():
    assert Checkout(StandardShipping()).shipping_cost(Order(750.0, 2.0)) == 49.0

def test_standard_shipping_is_free_at_exactly_1000():
    assert Checkout(StandardShipping()).shipping_cost(Order(1000.0, 2.0)) == 0.0

def test_standard_shipping_is_free_at_1000_or_more():
    assert Checkout(StandardShipping()).shipping_cost(Order(1250.0, 3.5)) == 0.0

def test_express_shipping_uses_base_plus_weight():
    assert Checkout(ExpressShipping()).shipping_cost(Order(500.0, 3.5)) == 141.0

def test_pickup_is_free():
    assert Checkout(PickupShipping()).shipping_cost(Order(500.0, 3.5)) == 0.0

def test_same_day_shipping_uses_base_plus_weight():
    assert Checkout(SameDayShipping()).shipping_cost(Order(500.0, 3.5)) == 212.0

def test_total_adds_shipping_cost():
    assert Checkout(StandardShipping()).total(Order(500.0, 2.0)) == 549.0

def test_checkout_delegates_to_any_strategy_without_changes():
    checkout = Checkout(ExampleShipping())
    assert checkout.shipping_cost(Order(subtotal=100.0, weight_kg=2.0)) == 10.0
    assert checkout.total(Order(subtotal=100.0, weight_kg=2.0)) == 110.0