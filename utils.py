import numpy as np
from itertools import combinations


def prime_numbers(n):
    i = 0
    all_numbers = np.arange(2, n)
    num_list = list(range(2, n))
    for num in all_numbers[:int(np.sqrt(n)+1)]:
        i += 1
        prime_array = all_numbers[:i]
        supp = all_numbers[i:][all_numbers[i:]%num!=0]
        all_numbers = np.concatenate([prime_array, supp])
    return all_numbers

def rSubset(numbers, r): 
    return list(map(list, combinations(numbers, r)))


def get_prime_factors(n, primes):
    p_list = []
    supp_n = n
    it = 0
    while supp_n!=1 and it<1000:
        for prime in primes:
            if supp_n%prime==0:
                supp_n /= prime
                p_list.append(prime)
                break
        it += 1
    return p_list


def get_divisors(n, all_primes):
    primes = all_primes[all_primes<=int(n/2+1)]
    p_list = get_prime_factors(n, primes)
    divisors = []

    for i in range(1, len(p_list)):
        list_numbers = rSubset(p_list, i)
        divisors += list(np.prod(list_numbers, axis=1))

    divisors = [1] + list(set(divisors))
    return divisors