import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def decimal_to_prime(decimal):
    integer = int(decimal * 10**5)
    primes = []
    for i in range(integer, integer + 10**5):
        if is_prime(i):
            primes.append(i)
    return primes

print(decimal_to_prime(math.sqrt(2) - int(math.sqrt(2))))
