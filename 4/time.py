import decimal
import time
from sympy.ntheory.primetest import isprime

def func_speed(func, *args, **kw):
    start_time = time.time()
    result = func(*args, **kw)
    print('time: {:.9f} [sec]'.format(time.time() - start_time))
    return result

decimal.getcontext().prec = 100


def sqrt2(): # √２の精度の高い表示
    return decimal.Decimal(2).sqrt()


def is_prime(n): # 素数判定　エラトステネスのふるい
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime():
    ans = []
    sqrt2_str = str(sqrt2())[2:] # 1.414...から整数部分を除いた部分
    for i in range(len(sqrt2_str) - 10): # 参照が後ろに行き過ぎるとバグるので、最後を手前に
        num = int(sqrt2_str[i:i+11]) # n個から11個をとってくる
        if isprime(num) & len(str(num)):
            ans.append(str(i))
            ans.append(str(num))
    return ans

func_speed(sqrt2)
func_speed(is_prime,85696718753)
func_speed(find_prime)