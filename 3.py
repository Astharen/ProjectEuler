import numpy as np
from utils import prime_numbers, get_prime_factors

n = 600851475143
prime_list = prime_numbers(int(np.sqrt(n) + 1))

print(np.max(get_prime_factors(n, prime_list)))