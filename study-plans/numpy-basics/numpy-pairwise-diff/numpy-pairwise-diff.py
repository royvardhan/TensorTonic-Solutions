import numpy as np

def pairwise_diff(a):
    """Returns: np.ndarray of shape (n, n) where out[i,j] = a[i] - a[j]"""
    b = np.array(a)
    diff = b[:, None] - b[None, :]
    return diff