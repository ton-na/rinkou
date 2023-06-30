import decimal
from sympy.ntheory.primetest import isprime

decimal.getcontext().prec = 1000

def sqrt2(): # √２の精度の高い表示
    return decimal.Decimal(2).sqrt()

def find_prime():
    ans = []
    sqrt2_str = str(sqrt2())[2:] # 1.414...から整数部分を除いた部分
    for i in range(len(sqrt2_str) - 10): # 参照が後ろに行き過ぎるとバグるので、最後を手前に
        num = int(sqrt2_str[i:i+11]) # n個から11個をとってくる
        if isprime(num) & len(str(num)): # メルセンヌ数などの特殊な数字を除いた中で一番早い素数判定アルゴリズム,AKS素数判定法
            ans.append(str(i))
            ans.append(str(num))
    return ans

print(find_prime())