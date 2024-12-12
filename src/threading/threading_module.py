import threading
import time


def print_numbers(thread_name, delay):
    for i in range(5):
        time.sleep(delay)
        print(f"{thread_name}")


thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 1))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 2))

thread1.start()
thread2.start()

thread1.join()
thread1.join()

print("Main Thread exiting")


class PrintNumbersThread(threading.Thread):
    def __init__(self, thread_name, delay):
        """Most Important Line"""
        super().__init__()
        self.thread_name = thread_name
        self.delay = delay

    """Most imp override the run method and call start from obj"""

    def run(self):
        for i in range(5):
            time.sleep(self.delay)
            print(f"{self.thread_name}:{i}")


thread1 = PrintNumbersThread("Thread1", 1)
thread2 = PrintNumbersThread("Thread2", 2)

thread1.start()
thread2.start()
thread1.join()
thread1.join()
