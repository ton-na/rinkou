import decimal

decimal.getcontext().prec = 100

def sqrt2():
    return decimal.Decimal(2).sqrt()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime():
    ans = []
    sqrt2_str = str(sqrt2())[2:]
    for i in range(len(sqrt2_str) - 10):
        num = int(sqrt2_str[i:i+11])
        if is_prime(num) & len(str(num)):
            ans.append(str(i))
            ans.append(str(num))
    return ans

print(find_prime())
