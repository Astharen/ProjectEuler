import numpy as np

def divisible_by_all_num_until_n(num, n):

    divisible_by = 0
    divisible = False
    for i in range(2, n+1):
        if num%i==0:
            divisible_by += 1
        else:
            break

    if divisible_by==(n-1):
        divisible = True
    return divisible

def smallest_positive_num_even_divisible_all_num_until_n(n):
    num = 20
    end = False
    max_it = 1
    for i in range(2, n+1):
        max_it *= i
    it = 0
    while not end and it<=max_it:
        
        num += 1
        
        if divisible_by_all_num_until_n(num , n):
            end = True
        it += 1
    return num

# print(divisible_by_all_num_until_n(2520 , 10))
# print(smallest_positive_num_even_divisible_all_num_until_n(10))

def positive_num_even_divisible_all_num_until_n(n):
    max_n = 1
    for i in range(2, 13):
        max_n *= i
    
    all_num = np.arange(1, max_n)
    divisible_array = all_num.copy()
    for i in range(2, n+1):
        divisible_array = divisible_array[divisible_array%i==0]
    return divisible_array

print(positive_num_even_divisible_all_num_until_n(20))