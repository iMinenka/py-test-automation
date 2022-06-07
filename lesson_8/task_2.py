"""1.	Decorator with parameters.
Реализуйте @timeit() декоратор который может принимать необязательный параметр threshold и покройте его юнит-тестами.

Пример:
@timeit(threshold=0.5)
def some_heavy_function():
    # complecated code goes here
    pass

@timeit()
def another_function():
    pass

Примечания:
•	параметр threshold принимает значение в секундах
•	декоратор должен печатать время выполнения если оно превышает значение указаное в threshold
•	если threshold не указан - декоратор должен печатать любое время выполнения
"""
from time import time


def timeit(threshold=0.0):
    """Capture execution time of a function. Print the time if function execution time is bigger than threshold.
    :param float threshold: execution threshold.
    """
    def inner(func):
        def wrapper(*args):
            start_time = time()
            result = func(*args)
            exec_time = round(time() - start_time, 2)
            if exec_time > threshold:
                print(f'{func.__name__} = {exec_time} secs')
            return result

        return wrapper

    return inner


@timeit(threshold=0.5)
def some_heavy_function():
    # complecated code goes here
    pass


@timeit()
def another_function():
    pass
