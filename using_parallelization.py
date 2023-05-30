import threading
from without_parallelization import build_factor_base, solution_linear_equations, calculate_log, timeit_decorator

@timeit_decorator
def main(S):
    threads = []
    lock = threading.Lock()
    result_found = threading.Event()
    result = None

    def thread_function():
        nonlocal result_found
        nonlocal result

        res = solution_linear_equations(alpha, n, S)
        lock.acquire()

        if not result_found.is_set():
            result = res
            result_found.set()

        lock.release()

    for _ in range(6):
        thread = threading.Thread(target=thread_function)
        threads.append(thread)
        thread.start()

    result_found.wait()

    for thread in threads:
        thread.join()

    return result

def start(c=3.38):      
    S = build_factor_base(n,c)
    equation = main(S)
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
    c += 0.1
    fun = start(c)

print(fun)