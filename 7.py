import numpy as np
from utils import prime_numbers_2

max_n = 1
for i in range(2, 13):
    max_n *= i

max_n *= 2

print(prime_numbers_2(max_n)[10001])