from my_thread import MyThread
from time import ctime, sleep


# Define the functions
def fib(x: int) -> int:
    # sleep(0.005)  # Simulate a delay
    if x < 2:
        return 1
    return fib(x - 2) + fib(x - 1)


def fac(x: int) -> int:
    # sleep(0.1)  # Simulate a delay
    if x < 2:
        return 1
    return x * fac(x - 1)


def summation(x: int) -> int:
    # sleep(0.1)  # Simulate a delay
    if x < 2:
        return 1
    return x + summation(x - 1)


def main():
    # List of functions
    funcs = [fib, fac, summation]
    n = 12  # Argument to pass to each function
    print('*** SINGLE THREAD')
    for func in funcs:
        print(f'Starting {func.__name__} at: {ctime()}')
        result = func(n)
        print(f'{func.__name__} result: {result}')
        print(f'{func.__name__} finished at: {ctime()}')

    print('\n*** MULTIPLE THREADS')
    threads = []
    for func in funcs:
        t = MyThread(func, (n,), func.__name__)
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()
        print(f'{t.name} result: {t.get_result()}')

    print('All done at:', ctime())


if __name__ == '__main__':
    main()
