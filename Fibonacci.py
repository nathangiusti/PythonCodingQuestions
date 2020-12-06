import time


def fibonacci(n):
    if n in [0, 1]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(1, 50):
    start_time = time.time()
    fibonacci(i)
    print("{}, {}".format(i, time.time() - start_time))