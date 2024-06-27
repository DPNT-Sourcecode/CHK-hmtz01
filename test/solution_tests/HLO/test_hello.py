from solutions.HLO import hello_solution
from hypothesis import given, strategies as st

@given(st.text())
def test_hello_contains_name(n):
    assert n in hello_solution.hello(n)

@given(st.text())
def test_hello_contains_hello(n):
    assert "Hello" in hello_solution.hello(n)

def test_hello_example(n):
    assert hello_solution.hello("John") == "Hello, John!"
