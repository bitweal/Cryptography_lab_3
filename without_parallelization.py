import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def build_factor_base(n, c=3.38):
    B = int(c * math.exp(math.sqrt(math.log(n) * math.log(math.log(n)))//2))
    factor_base = []
    for p in range(2, B):
        if is_prime(p):
            factor_base.append(p)
    return factor_base


alpha = int(input('Enter alpha: '))
beta = int(input('Enter beta: '))
n = int(input('Enter n: '))
S = build_factor_base(n)
print(S)