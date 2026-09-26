import numpy as np

def gradient_descent_step(values: list, gradients: list, learning_rate: float) -> tuple[list, float]:
    """
    Returns a fresh list of updated values and the predicted objective change.
    """
    new_list = list()
    change = 0.0
    for i in range(len(values)):
        new_value = values[i] - learning_rate * gradients[i]   # step against the gradient
        new_list.append(float(new_value))
        change += gradients[i] * (new_value - values[i])       # gradient × how far it moved
    return (new_list, float(change))
