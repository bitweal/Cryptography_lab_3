import math
import random
import numpy as np
import time

def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("The function {} was executed in {:.2f} seconds".format(func.__name__, execution_time))
        return result
    return wrapper

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

def is_smooth(alpha, S, n):
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

def find_solutions(equations, n, pre_coefficients=None, pre_constants=None):  
    equations_array = np.array(equations)    
    coefficients = equations_array[:, 1:]
    constants = equations_array[:, 0]                                                       
    try:
        solution = np.linalg.solve(coefficients, constants)
        if check_floating_point_numbers(solution):
            return None, coefficients, constants
        if pre_coefficients != None:
            for i in range(len(pre_coefficients)):
                if np.allclose(np.dot(pre_coefficients[i], solution)%n, pre_constants[i]%n) == False:
                    return None, coefficients, constants
            solution = np.remainder(solution, n)
            return solution.tolist(), pre_coefficients, pre_constants
        return None, coefficients, constants
    except np.linalg.LinAlgError:
         return None, coefficients, constants

def generate_combinations(matrix, new_rows):
    combinations = []

    for new_row in new_rows:
        for i in range(len(matrix)):
            new_matrix = [row[:] for row in matrix]  
            new_matrix[i] = new_row  
            combinations.append(new_matrix)

    return combinations

def solution_linear_equations(alpha, n, S):
    linear_equations = []
    new_row = []
    pre_coefficients = []
    pre_constants = []
    check = 0
    c = 0
    while c in range(len(S)+int(math.sqrt(n))+10):
        smooth_number = is_smooth(alpha, S, n)
        if smooth_number == None or smooth_number in linear_equations or smooth_number in new_row:
            continue
        else:
            if check < len(S):
                c += 1
                check += 1
                linear_equations.append(smooth_number)
                continue
            elif check == len(S):
                check += 1
                c += 1
                solution, pre_coe, pre_con = find_solutions(linear_equations, n - 1)
                pre_coefficients.append(pre_coe)
                pre_constants.append(pre_con)
            else:
                c += 1
                new_row.append(smooth_number)
                combo = generate_combinations(linear_equations, new_row)   
                linear_equations = combo[random.randint(-len(S), -1)]
                for i in combo:   
                    solution, pre_coe, pre_con = find_solutions(i, n - 1, pre_coefficients, pre_constants)
                    pre_coefficients.append(pre_coe)
                    pre_constants.append(pre_con)   
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

@timeit_decorator
def start(c=3.38):      
    S = build_factor_base(n,c)
    equation = solution_linear_equations(alpha, n, S)
    if equation == None:
        return "I can't found solution"
    else:
        while True:
            result = calculate_log(alpha, beta, n, S, equation)
            if result is None:
                continue
            else:
                return result


alpha = int(input('Enter alpha: '))
beta = int(input('Enter beta: '))
n = int(input('Enter n: '))
fun = start()
c = 3.38 
while type(fun) is not int and c <= 7:
    c += 0.2
    fun = start(c)

print(fun)