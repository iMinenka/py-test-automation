"""2.	Context manager.
Реализуйте контекстный менеджер timer, используя __enter__ и __exit__

Check yourself:

with timer('doing some sleeps'):
    time.sleep(1)
    time.sleep(2)
    time.sleep(3)

Output:
timer: block 'doing some sleeps' executed in 6.013 sec
"""
import time


class Timer:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        exec_time = round(self.end - self._start, 3)
        print(f"Timer: block '{self.name}' executed in {exec_time} sec")


if __name__ == '__main__':
    with Timer('doing some sleeps'):
        time.sleep(1)
        time.sleep(2)
        time.sleep(3)