import numpy as np

def mean_squared_error(y_pred, y_true):
    error = 0
    n = len(y_true)
    for i ,j in zip(y_pred, y_true):
        error += (j-i)**2

    return error/n