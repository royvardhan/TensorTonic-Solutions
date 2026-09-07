import numpy as np

def scale_cols(data, weights):
    """Returns: np.ndarray of shape (m, n), each column scaled by corresponding weight"""
    data = np.array(data)
    weights = np.array(weights)

    return data * weights