import math
from sympy import primerange

def is_prime(num):
    n = int(math.sqrt(num)) + 1
    primlist = list(primerange(2,n))

    if num < 2:
        return False
    for i in primlist:
        if num % i == 0:
            return False
    return True

def decimal_to_prime(decimal):
    integer = int(decimal * 10**11)
    primes = []
    for i in range(integer, integer + 10**11):
        if is_prime(i):
            primes.append(i)
            if len(str(i)) == 11:
                return i
    return None

print(decimal_to_prime(math.sqrt(2) - int(math.sqrt(2))))
