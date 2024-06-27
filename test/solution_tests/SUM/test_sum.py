from solutions.SUM import sum_solution
from hypothesis import given, strategies as st

def test_sum():
    assert sum_solution.compute(1, 2) == 3

@given(st.integers(min_value=0, max_value=100), st.integers(min_value=0, max_value=100))
def test_sum_ints_is_int(x, y):
    assert isinstance(sum_solution.compute(x, y), int)


