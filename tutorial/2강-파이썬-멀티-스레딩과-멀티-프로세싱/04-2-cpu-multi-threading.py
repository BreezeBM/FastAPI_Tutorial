import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor

nums = [12, 7, 2]


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread, {num}")

    numbers = range(1, num)
    total = 1

    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k

    return total


def main():
    executor = ThreadPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)

# 초 걸림
