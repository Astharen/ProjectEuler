import numpy as np


def sum_square_n_natural_number(n):
    return np.sum(np.arange(1,n+1)**2)


def square_sum_n_natural_number(n):
    return np.sum(np.arange(1,n+1))**2


def diference_square_sum_sum_square(n):
    return square_sum_n_natural_number(n) - sum_square_n_natural_number(n)


print(diference_square_sum_sum_square(100))