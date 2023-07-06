import decimal
from sympy.ntheory.primetest import isprime
decimal.getcontext().prec = 100
sqrt2_str = str(decimal.Decimal(2).sqrt())[2:] # 1.414...から整数部分を除いた部分
print([str(i) +"番目: "+ str(int(sqrt2_str[i:i+11])) for i in range(len(sqrt2_str) - 10) if isprime(int(sqrt2_str[i:i+11])) & len(str(int(sqrt2_str[i:i+11])))])