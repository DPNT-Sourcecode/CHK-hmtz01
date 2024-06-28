from solutions.CHK import checkout_solution
from hypothesis import given, strategies as st
import pytest

@pytest.mark.parametrize(
    "input_skus, counter_output",
    [
        ("A", {"A": 1}),
        ("B", {"B": 1}),
        ("ABAC", {"A": 2, "B": 1, "C": 1}),
        ("ABDDDACC", {"A": 2, "B": 1, "C": 2, "D": 3}),
    ]
)
def test_checkout_counter(input_skus, counter_output):
    assert checkout_solution.counter(input_skus) == counter_output


@pytest.mark.parametrize(
    "input_basket, price",
    [
        ({"A": 3}, 130),
        ({"A": 1}, 50),
        ({"B": 2}, 45),
        ({"C": 1}, 20),
        ({"D": 1}, 15),
    ]
)
def test_price_step(input_basket, price):
     new_price, new_basket = checkout_solution.price_step(1000, input_basket)
     assert new_price == 1000 + price
     assert sum(new_basket.values()) == 0


