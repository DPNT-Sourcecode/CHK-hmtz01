from solutions.CHK import checkout_solution
from hypothesis import given, strategies as st
import pytest

@pytest.mark.parametrize(
    "input_skus, expected_total",
    [
        ("A", 50),
        ("B", 30),
        ("AABAC", 180),
        ("AABBBAACD", 130 + 50 + 45 + 30 + 20 + 15),
        ("ABCDE", -1)
    ]
)
def test_checkout_examples(input_skus, expected_total):
    assert checkout_solution.checkout(input_skus) == expected_total



@pytest.mark.parametrize(
    "input_skus, counter_output",
    [
        ("A", {"A": 1}),
        ("B", {"B": 1}),
        ("ABAC", {"A": 2, "B": 1, "C": 1}),
        ("ABDDDACC", {"A": 2, "B": 1, "C": 2, "D": 3}),
    ]
)
def test_basket_from_skus(input_skus, counter_output):
    assert checkout_solution.basket_from_skus(input_skus) == counter_output


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
     # Check price has incremented correctly
     assert new_price == 1000 + price
     # Check that basket is empty
     assert sum(new_basket.values()) == 0





