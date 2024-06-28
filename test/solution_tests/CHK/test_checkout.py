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

