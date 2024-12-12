import threading
from typing import Callable, Any
from time import ctime

class MyThread(threading.Thread):
    def __init__(self, func: Callable, args: tuple, name: str = ''):
        super().__init__()
        self.func = func
        self.args = args
        self.name = name
        self.res = None

    def get_result(self) -> Any:
        return self.res

    def run(self):
        print(f'Starting {self.name} at: {ctime()}')
        self.res = self.func(*self.args)
        print(f'{self.name} finished at: {ctime()}')
