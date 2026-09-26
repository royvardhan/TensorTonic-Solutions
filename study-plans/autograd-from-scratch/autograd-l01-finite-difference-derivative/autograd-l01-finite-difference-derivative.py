import numpy as np

def finite_difference_derivative(coefficients: list, x: float, h: float) -> tuple[float, float, float]:
    """
    Returns the value at x, the value at x plus h, and the estimated slope.
    """
    coeffs = list(reversed(coefficients))
    fx = float(np.polyval(coeffs, x))
    fxh = float(np.polyval(coeffs, x + h))
    slope = (fxh - fx) / h

    return (fx, fxh, slope)
