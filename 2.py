import numpy as np


def fibonacci_numbers(n):
    fibonacci_dict = {}
    i = 0
    end = False
    while not end:
        if i == 0:
            fibonacci_dict[0] = 1
        elif i == 1:
            fibonacci_dict[1] = 2
        else:
            fibonacci_dict[i] = fibonacci_dict[i-1] + fibonacci_dict[i-2]
            if fibonacci_dict[i-1] + fibonacci_dict[i-2] >= n:
                end = True
        i += 1
    return fibonacci_dict


def sum_even_fib_num(n):
    fibonacci_dict = fibonacci_numbers(n)
    fib_array = np.array(list(fibonacci_dict.values()))
    supp = fib_array[fib_array%2==0]
    return np.sum(supp)

print(sum_even_fib_num(4_000_000))