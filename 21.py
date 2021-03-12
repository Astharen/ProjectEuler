import numpy as np
from utils import prime_numbers, rSubset, get_prime_factors, get_divisors


def dict_sum_divisors(n):
    all_primes = prime_numbers(n)
    sum_divisors = {}

    for num in range(2, (n+1)):
        if num not in all_primes:
            divisors = get_divisors(num, all_primes)
            sum_divisors[num] = np.sum(divisors)
    return sum_divisors


def get_amicables(n):
    sum_divisors = dict_sum_divisors(n)
    list_amicables = []
    values_taken = []

    for k, v in sum_divisors.items():
        if k != v:
            if v in sum_divisors.keys() and k not in values_taken and v not in values_taken:
                supp_value = sum_divisors[v]
                if supp_value == k:
                    list_amicables.append([k, v])
                    values_taken.append(v)
                    values_taken.append(k)

    return list_amicables


def get_all_amicables_sum(list_amicables):
    all_amicables_sum = np.sum(np.sum(list_amicables))
    return all_amicables_sum


n = 10_000

list_amicables =  get_amicables(n)
print(list_amicables)

print(get_all_amicables_sum(list_amicables))

#print(dict_sum_divisors(n))