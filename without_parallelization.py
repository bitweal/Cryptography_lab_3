import math
import random
import numpy as np
from sympy import symbols, Eq, solve

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
    a = pow(alpha, k, n)
    power = [k]
    for p in S:
        c_power = 0
        while a % p == 0:
            a //= p        
            c_power += 1
        power.append(c_power)

    if all(value == 0 for value in power[1:]): 
        return None
    else:
        return power

def find_solutions(equations, n):  
    equations_array = np.array(equations)    
    coefficients = equations_array[:, 1:]
    constants = equations_array[:, 0]  

    if np.any(np.all(equations_array == 0, axis=0)):
        return None

    zero_columns = np.where(np.all(coefficients == 0, axis=0))[0]  
    if len(zero_columns) > 0:
        coefficients = np.delete(coefficients, zero_columns, axis=1)
        num_variables = coefficients.shape[1]
   
    try:
        solution = np.linalg.lstsq(coefficients, constants, rcond=-1)[0]
        #print(solution)
        solution = np.remainder(solution, n)
        return solution.tolist()
    except np.linalg.LinAlgError:
        return None

def solution_linear_equations(alpha, n, S):
    linear_equations = []
    for c in range(len(S)+15):
        smooth_number = is_smooth(alpha, S)
        if smooth_number == None:
            continue
        else:
            linear_equations.append(smooth_number)           
            #linear_equations = [[1,1,0,1,0],[2,1,1,0,0],[6,2,0,0,1],[7,0,2,1,0]]
            print(linear_equations)
            solution = find_solutions(linear_equations, n-1)
            print(solution)
            if type(solution) == list:
                break
               
    return solution

def calculate_log(alpha, beta, n, S, equation):
    l = random.randint(0, n-1)
    #equation = [30,18,17,38]
    #l = 2
    number = beta * pow(alpha, l) % n
    print(l)
    print(number)
    power = []
    for p in S:
        c_power = 0
        while number % p == 0:
            number //= p        
            c_power += 1
        power.append(c_power)

    if all(value == 0 for value in power) or number != 1: 
        return None
    print(power)
    result = 0
    for i in range(len(S)):
        if power[i] != 0:
            result += (power[i] * equation[i]) % (n-1)

    return (result - l) % (n-1)
    
alpha = int(input('Enter alpha: '))
beta = int(input('Enter beta: '))
n = int(input('Enter n: '))
S = build_factor_base(n)
print(S)
equation = solution_linear_equations(alpha, n, S)
result = calculate_log(alpha, beta, n, S, equation)

print(result)