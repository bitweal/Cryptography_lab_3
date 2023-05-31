import multiprocessing
from without_parallelization import build_factor_base, solution_linear_equations, calculate_log, timeit_decorator

def process_function(result_queue, result_found, alpha, n, S):
    res = solution_linear_equations(alpha, n, S)
    if not result_found.is_set():
        result_queue.put(res)
        result_found.set()

def main(S):
    processes = []
    result_found = multiprocessing.Event()
    result_queue = multiprocessing.Queue()

    for _ in range(6):
        process = multiprocessing.Process(target=process_function, args=(result_queue, result_found, alpha, n, S))
        processes.append(process)
        process.start()

    result = result_queue.get()
    result_found.set()

    for process in processes:
        process.join()

    return result

@timeit_decorator
def start(c=3.38):
    S = build_factor_base(n, c)
    equation = main(S)
    if equation is None:
        return "I can't find a solution"
    else:
        while True:
            result = calculate_log(alpha, beta, n, S, equation)
            if result is None:
                continue
            else:
                return result

if __name__ == '__main__':
    alpha = int(input('Enter alpha: '))
    beta = int(input('Enter beta: '))
    n = int(input('Enter n: '))
    fun = start()
    c = 3.38

    while not isinstance(fun, int) and c <= 7:
        c += 0.1
        fun = start(c)

    print(fun)