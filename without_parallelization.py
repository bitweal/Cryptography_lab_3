from itertools import combinations
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

    if all(value == 0 for value in power[1:]) or a > 1: 
        return None
    else:
        return power

def check_floating_point_numbers(lst):
    found_floating_point = False

    for item in lst:
        if isinstance(item, float) and not item.is_integer():
            found_floating_point = True
            break

    if found_floating_point:
        return True
    else:
        return False

def find_solutions(equations, n):  
    equations_array = np.array(equations)    
    coefficients = equations_array[:, 1:]
    constants = equations_array[:, 0]  

    for j in range(1,len(equations[0])):
        not_zero = False
        for i in range(len(equations)):
            if equations[i][j] != 0:
                not_zero = True
        if not_zero  == False:
            return None
            
    try:
        solution = np.linalg.solve(coefficients, constants)
        if np.allclose(np.dot(coefficients, solution), constants) == False \
            or check_floating_point_numbers(solution) :
            return None
        solution = np.remainder(solution, n)
        return solution.tolist()
    except np.linalg.LinAlgError:
        return None

def generate_combinations(matrix, row):
    combinations = []
    n = len(matrix) 
    for i in range(n):
        new_matrix = []
        for idx in range(n):
            if idx == i:
                new_matrix.append(row[:])
            else:
                new_matrix.append(matrix[idx])

        combinations.append(new_matrix)

    return combinations

def solution_linear_equations(alpha, n, S):
    linear_equations = []
    solution = []
    check = 0
    c = 0
    while c in range(len(S)+15):
        smooth_number = is_smooth(alpha, S)
        if smooth_number == None or smooth_number in linear_equations:
            continue
        else:
            if check < len(S):
                check += 1
                linear_equations.append(smooth_number)
                c += 1
                continue
            elif check == len(S):
                check += 1
                c += 1
                solution = find_solutions(linear_equations, n-1)
            else:
                c += 1
                combo = generate_combinations(linear_equations, smooth_number)
                for i in combo:
                    solution = find_solutions(i, n-1)
                    if type(solution) == list:
                        return solution
            if type(solution) == list:
                return solution
    return None

def calculate_log(alpha, beta, n, S, equation):
    l = random.randint(0, n-1)
    number = beta * pow(alpha, l) % n
    power = []
    for p in S:
        c_power = 0
        while number % p == 0:
            number //= p        
            c_power += 1
        power.append(c_power)
    if all(value == 0 for value in power) or number > 1: 
        return None
    result = 0
    for i in range(len(S)):
        if power[i] != 0:
            result += (power[i] * equation[i]) % (n-1)

    return int((result - l) % (n-1))
    
alpha = int(input('Enter alpha: '))
beta = int(input('Enter beta: '))
n = int(input('Enter n: '))
S = build_factor_base(n)
equation = solution_linear_equations(alpha, n, S)
if equation == None:
    print("I can't found solution")
else:
    while True:
        result = calculate_log(alpha, beta, n, S, equation)
        if result is None:
            continue
        else:
            print(result)
            break