# Open a file, read from it, and automatically close it when done
from typing import ContextManager

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)


# Custom Context Manager basically auto-closable like java

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting the Context Manager')
        if exc_type:
            print(f"An Exception Occurred {exc_val}")
        else:
            print("No Exceptions Occurred")


with MyContextManager() as cm:
    print("I am inside context")
