import numpy as np

def norm_gate(X: list, W: list, threshold: float) -> np.ndarray:
    """
    Returns an (n, k) float64 matrix of norm-gated transformed rows.
    """
    Z = np.array(X, dtype=np.float64) @ np.array(W, dtype=np.float64)
    norms = np.linalg.norm(Z, axis=1)
    return np.where(norms[:, np.newaxis] >= threshold, Z, 0.0)
