from concurrent.futures import ThreadPoolExecutor

# A simple function that just prints a message
def greet(name):
    print(f"Hello, {name}!")

def main():
    # Create a thread pool with 2 threads
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks (greet function with different names)
        executor.submit(greet, "Alice")
        executor.submit(greet, "Bob")

    # The executor will automatically shut down here after the 'with' block ends

if __name__ == "__main__":
    main()
