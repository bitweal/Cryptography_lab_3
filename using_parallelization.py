import threading
from without_parallelization import build_factor_base, solution_linear_equations, calculate_log

def main():
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

    for _ in range(4):
        thread = threading.Thread(target=thread_function)
        threads.append(thread)
        thread.start()

    result_found.wait()

    for thread in threads:
        thread.join()

    return result

alpha = int(input('Enter alpha: '))
beta = int(input('Enter beta: '))
n = int(input('Enter n: '))
S = build_factor_base(n, 100)
print(S)

equation = main()

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