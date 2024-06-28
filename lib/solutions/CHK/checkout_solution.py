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
    f = basket.get("F", 0)
    g = basket.get("G", 0)
    h = basket.get("H", 0)
    i = basket.get("I", 0)
    j = basket.get("J", 0)
    k = basket.get("K", 0)
    l = basket.get("L", 0)
    m = basket.get("M", 0)
    n = basket.get("N", 0)
    o = basket.get("O", 0)
    p = basket.get("P", 0)
    q = basket.get("Q", 0)
    r = basket.get("R", 0)
    s = basket.get("S", 0)
    t = basket.get("T", 0)
    u = basket.get("U", 0)
    v = basket.get("V", 0)
    w = basket.get("W", 0)
    x = basket.get("X", 0)
    y = basket.get("Y", 0)
    z = basket.get("Z", 0)

    if e >= 2 and b >= 1:
        return (subtotal + 80, {**basket, "E": e - 2, "B": b - 1})
    if f >= 3:
        return (subtotal + 20, {**basket, "F": f - 3})
    if a >= 5:
        return (subtotal + 200, {**basket, "A": a - 5})
    if a >= 3:
        return (subtotal + 130, {**basket, "A": a - 3})
    if b >= 2:
        return (subtotal + 45, {**basket, "B": b - 2})
    if h >= 10:
        return (subtotal + 80, {**basket, "H": h - 10})
    if h >= 5:
        return (subtotal + 45, {**basket, "H": h - 5})
    if k >= 2:
        return (subtotal + 150, {**basket, "K": k - 2})
    if n >= 3 and m >= 1:
        return (subtotal + 120, {**basket, "N": n - 3, "M": m - 1})
    if p >= 5:
        return (subtotal + 200, {**basket, "P": p - 5})
    if r >= 3 and q >= 1:
        return (subtotal + 150, {**basket, "R": r - 3, "Q": q - 1})
    if q >= 3:
        return (subtotal + 80, {**basket, "Q": q - 3})
    if u >= 4:
        return (subtotal + 120, {**basket, "U": u - 4})
    if v >= 3:
        return (subtotal + 130, {**basket, "V": v - 3})
    if v >= 2:
        return (subtotal + 90, {**basket, "V": v - 2})
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
    if f >= 1:
        return (subtotal + 10, {**basket, "F": f - 1})
    if g >= 1:
        return (subtotal + 20, {**basket, "G": g - 1})
    if h >= 1:
        return (subtotal + 10, {**basket, "H": h - 1})
    if i >= 1:
        return (subtotal + 35, {**basket, "I": i - 1})
    if j >= 1:
        return (subtotal + 60, {**basket, "J": j - 1})
    if k >= 1:
        return (subtotal + 70, {**basket, "K": k - 1})
    if l >= 1:
        return (subtotal + 90, {**basket, "L": l - 1})
    if m >= 1:
        return (subtotal + 15, {**basket, "M": m - 1})
    if n >= 1:
        return (subtotal + 40, {**basket, "N": n - 1})
    if o >= 1:
        return (subtotal + 10, {**basket, "O": o - 1})
    if p >= 1:
        return (subtotal + 50, {**basket, "P": p - 1})
    if q >= 1:
        return (subtotal + 30, {**basket, "Q": q - 1})
    if r >= 1:
        return (subtotal + 50, {**basket, "R": r - 1})
    if s >= 1:
        return (subtotal + 20, {**basket, "S": s - 1})
    if t >= 1:
        return (subtotal + 20, {**basket, "T": t - 1})
    if u >= 1:
        return (subtotal + 40, {**basket, "U": u - 1})
    if v >= 1:
        return (subtotal + 50, {**basket, "V": v - 1})
    if w >= 1:
        return (subtotal + 20, {**basket, "W": w - 1})
    if x >= 1:
        return (subtotal + 17, {**basket, "X": x - 1})
    if y >= 1:
        return (subtotal + 20, {**basket, "Y": y - 1})
    if z >= 1:
        return (subtotal + 21, {**basket, "Z": z - 1})


    if all(v == 0 for v in basket.values()):
        return subtotal, None
    else:
        return -1, None

