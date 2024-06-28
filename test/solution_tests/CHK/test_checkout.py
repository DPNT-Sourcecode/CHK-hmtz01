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
        ("ABCDz", -1)
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
        ({"A": 5}, 200),
        ({"A": 3}, 130),
        ({"A": 1}, 50),
        ({"B": 2}, 45),
        ({"C": 1}, 20),
        ({"D": 1}, 15),
        ({"D": 1}, 15),
        ({"B": 1, "E": 2}, 80),
        ({"E": 1}, 40),
        ({"F": 3}, 20),
        ({"F": 1}, 10),
        ({"G": 1}, 20),
        ({"H": 1}, 10),
        ({"H": 10}, 80),
        ({"H": 5}, 45),
        ({"I": 1}, 35),
        ({"J": 1}, 60),
        ({"K": 2}, 150),
        ({"K": 1}, 80),
        ({"L": 1}, 90),
        ({"M": 1}, 15),
        ({"N": 3, "M": 1}, 120),
        ({"N": 1}, 40),
        ({"O": 1}, 10),
        ({"P": 5}, 200),
        ({"P": 1}, 50),
        ({"Q": 3}, 80),
        ({"Q": 1}, 30),
        ({"R": 3, "Q": 1}, 150),
        ({"R": 1}, 50),
        ({"S": 1}, 30),
        ({"T": 1}, 20),
        ({"U": 4}, 120),
        ({"U": 1}, 40),
        ({"V": 3}, 130),
        ({"V": 2}, 90),
        ({"V": 1}, 50),
        ({"W": 1}, 20),
        ({"X": 1}, 90),
        ({"Y": 1}, 10),
        ({"Z": 1}, 50),
    ]
)
def test_price_step(input_basket, price):
     new_price, new_basket = checkout_solution.price_step(1000, input_basket)
     # Check price has incremented correctly
     assert new_price == 1000 + price
     # Check that basket is empty
     assert sum(new_basket.values()) == 0


