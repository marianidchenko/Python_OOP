def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def get_primes(list):
    return(n for n in list if is_prime(n))

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))