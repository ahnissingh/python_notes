import threading
def example1():
    def sum_up_to_100():
        total = sum(range(1, 101))
        print(f"Sum of Numbers upto 100:{total}")

    thread1 = threading.Thread(target=sum_up_to_100)
    thread1.start()
    thread1.join()


def example2():
    def fibonacci(num):
        fib = [0, 1]
        for i in range(2, num):
            fib.append(fib[i - 1] + fib[i - 2])
        print(f"Fibonacci numbers up to {num}: {fib}")

    n = 10
    thread = threading.Thread(target=fibonacci, args=(n,))
    thread.start()
    thread.join()

