import math
import random

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

def is_smooth(alpha, S):
    k = random.randint(0, n-1)
    a = alpha**k % n
    power = []
    for p in S:
        c_power = 0
        while a % p == 0:
            a //= p        
            c_power += 1
        power.append(c_power)

    if all(value == 0 for value in power): 
        return None
    else:
        return power
    
def build_linear_equations(alpha, n, S):
    linear_equations = []
    for c in range(len(S)+15):
        smooth_number = is_smooth(alpha, S)
        if smooth_number == None:
            continue
        else:
            linear_equations.append(smooth_number)
    return linear_equations
    

alpha = int(input('Enter alpha: '))
beta = int(input('Enter beta: '))
n = int(input('Enter n: '))
S = build_factor_base(n)
equation = build_linear_equations(alpha, n, S)
print(equation)