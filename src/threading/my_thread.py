import threading
from typing import Callable, Any
from time import ctime, sleep


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        super().__init__()
        self.func = func
        self.args = args
        self.name = name
        self.res = None

    def get_result(self):
        return self.res

    def run(self):
        print(f'Starting {self.name} at: {ctime()}')
        self.res = self.func(*self.args)
        print(f'{self.name} finished at: {ctime()}')


def example_function(x, y):
    sleep(2)  # Simulating a time-consuming task
    return x + y


thread1 = MyThread(func=example_function, args=(10, 20), name="AdditionThread1")
thread2 = MyThread(func=example_function, args=(30, 40), name="AdditionThread2")

thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

# Get results
result1 = thread1.get_result()
result2 = thread2.get_result()

print(f"Result from {thread1.name}: {result1}")
print(f"Result from {thread2.name}: {result2}")
