import numpy as np


def get_multiples_of_x_below_n(n, x):
    sol_list = []
    for num in range(3, n):
        for i in x:
            if num%i==0 and num not in sol_list:
                sol_list.append(num)
    return sol_list


def sum_all(x):
    return np.sum(x)


n = 1000
x = [3, 5]

multiples = get_multiples_of_x_below_n(n, x)
print(sum_all(multiples))