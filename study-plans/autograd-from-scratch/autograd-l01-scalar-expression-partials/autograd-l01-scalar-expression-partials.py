def scalar_expression_partials(a: float, b: float, c: float, h: float) -> tuple[float, float, float, float]:
    """
    Returns the expression value and numerical partials for a, b, and c.
    """
    d = (a * b) + c
    na = ((a+h) * b) + c
    nb = (a * (b+h)) + c
    nc = (a * b) + (c + h)

    return (float(d), float((na - d) / h), float((nb - d) / h), float((nc - d) / h))
