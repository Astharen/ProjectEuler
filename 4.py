from utils import prime_numbers, get_prime_factors
import numpy as np


# min possible palindrome 100 * 100 = 10000 max possible palindrome = 999 * 999 = 998001

def get_palindromes_from_a_to_b():
    n = -1

    for n1 in range(100, 1000):
        for n2 in range(100, 1000):
            num = n1 * n2
            if str(num)==str(num)[::-1]:
                n = max(n, num)
    return n

largest_palindrome = get_palindromes_from_a_to_b()
print(largest_palindrome)