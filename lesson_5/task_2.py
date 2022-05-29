"""2.	Multiprocessing library.
Для решения задачи #5 (Multiples of 3 and 5) было реализовано множество различных алгоритмов.
В файле multiples_of_three_and_five.py перечислены наиболее популярные из них.

Давайте выясним какой из предложенных алгоритмов является самым эффективным.

Используйте библиотеку multiprocessing, чтобы запустить параллельное выполнение всех 4-х функций.
Вам также понадобится контекстный менеджер timer

Ответьте на вопрос:
•	почему мы не используем библиотеку threading для решения этой задачи?

Check yourself:

bash$ python multiples_of_three_and_five.py

Output:

math_formula() -> 0.0 sec
several_for_loops() -> 28.89 sec
iterate_over_fifteen() -> 41.32 sec
simple_iteration() -> 66.87 sec
"""
"""
These are different solutions of "Task 5: Multiples of 3 and 5. Find the best algorithm"

Let's find out which of the proposed algorithms is the most effective
"""

import multiprocessing
import time
from multiprocessing import Pool

N = 300000000


def simple_iteration():
    res = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


def several_for_loops():
    res = 0
    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    return res


def iterate_over_fifteen():
    range_diff = [0, 3, 5, 6, 9, 10, 12]
    res = 0
    for i in range(0, N, 15):
        for d in range_diff:
            v = i + d
            if v >= N:
                break
            res += v
    return res


def math_formula():
    upper = N - 1
    threes = int(3 * (upper / 3) * ((upper / 3) + 1) / 2)
    fives = int(5 * (upper / 5) * ((upper / 5) + 1) / 2)
    fifteens = int(15 * (upper / 15) * ((upper / 15) + 1) / 2)
    res = threes + fives - fifteens
    return res


class Timer:
    """This class is used as a context manager to calculate execution time of a function."""
    def __init__(self, some_function):
        """Get the function name.

        Args:
            some_function: function to retrieve the name using method __name__.

        """
        self.function_name = some_function.__name__

    def __enter__(self):
        """Pick the time when Timer is called."""
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Pick the time when Timer execution ended.
        Calculate difference between end and start time."""
        end = time.time()
        execution_time = round(end - self.start, 2)
        print(f"{self.function_name}() -> {execution_time} sec")


def time_wrapper(func):
    """Run the function in the context manager of class Timer."""
    with Timer(func):
        func()


def run_all_calculations_in_parallel():
    # Use multiprocessing library to run all above functions in parallel
    # Print execution time of each function

    functions_to_call = [simple_iteration, several_for_loops, iterate_over_fifteen, math_formula]

    # Option 1 - create process, start and stop all processes
    processes = []

    for function in functions_to_call:
        p = multiprocessing.Process(target=time_wrapper, args=(function,))
        p.start()
        processes.append(p)

    for ps in processes:
        ps.join()

    # # Option 2 - with Pool
    # with Pool(len(functions_to_call)) as p:
    #     p.map(time_wrapper, [simple_iteration, several_for_loops, iterate_over_fifteen, math_formula])


if __name__ == '__main__':
    run_all_calculations_in_parallel()
