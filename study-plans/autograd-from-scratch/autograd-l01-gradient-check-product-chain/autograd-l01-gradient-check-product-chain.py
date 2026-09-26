import numpy as np

def gradient_check_product_chain(
    a: float,
    b: float,
    c: float,
    f: float,
    h: float,
) -> tuple[float, list, list, float]:
    """
    Returns loss, analytic gradients, numerical gradients, and maximum error.
    """
    
    d = (a * b) + c
    L = d * f

    La = ((a + h) * b + c) * f
    Lb = (a * (b + h) + c) * f
    Lc = (a * b + (c + h)) * f
    Lf = d * (f + h)

    nl = [float((La - L) / h), float((Lb - L) / h), float((Lc - L) / h), float((Lf - L) / h)]
    al = [float(b * f), float(a * f), float(f), float(d)]

    max_diff = max(abs(x - y) for x, y in zip(al, nl))
    return (float(L), al, nl, float(max_diff))
    pass
