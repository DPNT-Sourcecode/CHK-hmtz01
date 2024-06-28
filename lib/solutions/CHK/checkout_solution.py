from collections import Counter
from dataclasses import dataclass

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = basket_from_skus(skus)
    subtotal = 0

    while basket is not None:
        subtotal, basket = price_step(subtotal, basket)

    return subtotal


def basket_from_skus(skus):
    """
    Count a total for each item in the basket
    """
    return Counter(skus)


def price_step(subtotal, basket):
    """
    Apply a single pricing step, returning the new subtotal, and unpriced basket.
    """
    a = basket.get("A", 0)
    b = basket.get("B", 0)
    c = basket.get("C", 0)
    d = basket.get("D", 0)
    e = basket.get("E", 0)

    if e >= 2 and b >= 1:
        return (subtotal + 80, {**basket, "E": e - 2, "B": b - 1})
    if f >= 3:
        return (subtotal + 30, {**basket, "F": f - 3})
    if a >= 5:
        return (subtotal + 200, {**basket, "A": a - 5})
    if a >= 3:
        return (subtotal + 130, {**basket, "A": a - 3})
    if b >= 2:
        return (subtotal + 45, {**basket, "B": b - 2})
    if a >= 1:
        return (subtotal + 50, {**basket, "A": a - 1})
    if b >= 1:
        return (subtotal + 30, {**basket, "B": b - 1})
    if c >= 1:
        return (subtotal + 20, {**basket, "C": c - 1})
    if d >= 1:
        return (subtotal + 15, {**basket, "D": d - 1})
    if e >= 1:
        return (subtotal + 40, {**basket, "E": e - 1})


    if all(v == 0 for v in basket.values()):
        return subtotal, None
    else:
        return -1, None



