import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    arr = np.array(data, dtype=np.float64)
    copied = arr[row_idx].copy()
    clipped = np.clip(copied, lo, hi)
    return np.stack([copied, clipped])
    