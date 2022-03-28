import numpy as np

def one_plus_log(x):
    return np.log(1 + x)

def one_plus_log_reverse(x):
    return np.exp(x) - 1