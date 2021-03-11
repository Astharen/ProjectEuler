from utils import prime_numbers


def is_prime(n):
    prime = True
    for num in range(2, int(n/2)):
        if n%num==0:
            prime = False
            break
    return prime

def test_list_prime(prime_numbers):
    not_prime = True
    ind = 0
    while not_prime and ind<=(prime_numbers.shape[0]-1):
        if not is_prime(prime_numbers[ind]):
            not_prime = False
            print(f'{prime_numbers[ind]} No es primo')
        ind += 1
    if not_prime:
        print('Son primos')


prime_num = prime_numbers(5000)

supp_array = np.concatenate([prime_num, np.array([4600])])
print(prime_num)

test_list_prime(prime_num)