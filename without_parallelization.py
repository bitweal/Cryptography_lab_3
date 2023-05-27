import math
import random
import numpy as np

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
  

def find_solutions(equations):
    equations_array = np.array(equations)    
    coefficients = equations_array[:, 1:]
    constants = equations_array[:, 0]  
    num_equations, num_variables = coefficients.shape
    
    if num_equations < num_variables:
        return None
   
    try:
        solution = np.linalg.lstsq(coefficients, constants, rcond=None)[0]
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
            print(linear_equations)
            solution = find_solutions(linear_equations)
            if type(solution) == list:
                break
               
    return solution   

alpha = int(input('Enter alpha: '))
beta = int(input('Enter beta: '))
n = int(input('Enter n: '))
S = build_factor_base(n)
equation = solution_linear_equations(alpha, n, S)

print(equation)