import _thread
import time


def print_numbers(thread_name, delay):
    for i in range(5):
        time.sleep(delay)
        print(f"{thread_name}:{i}")


_thread.start_new_thread(print_numbers, ("Thread1", 1))
_thread.start_new_thread(print_numbers, ("Thread2", 2))

time.sleep(6)  # Allow time for threads to finish
print("Main Thread is exiting")

#ISSUES
"""
1)Low Level API: The _thread module provides only basic functionalities for creating and managing threads, such as starting a thread and exiting.
2) No Support for Thread Synchronization:Unlike the threading module, _thread does not provide mechanisms like Lock, RLock, Semaphore, or Condition for synchronizing access to shared resources. You must implement synchronization manually, increasing the risk of race conditions.
3Risk of Deadlocks and Race Conditions:Without thread synchronization primitives, managing shared resources becomes error-prone, leading to deadlocks (when two or more threads block each other indefinitely) or race conditions (when threads access shared data in an unpredictable order).
4) No Thread Object : _thread does not represent threads as objects. Instead, it works with basic functions, making it harder to control or monitor individual threads.
5) No Thread Lifecycle Control:_thread lacks functionality to explicitly join threads (i.e., wait for a thread to complete before continuing execution).
6) No Daemon Threads:_thread does not have support for daemon threads. A daemon thread is one that runs in the background and is automatically terminated when the main thread exits. Without this feature, managing background tasks becomes more complex.
7)Less Readable Code:Code written with _thread is often harder to read and maintain, especially in programs with complex thread interactions, due to the lack of higher-level abstractions.
8)Deprecation in Practice:While _thread is generally not recommended, it might be useful for:Low-level or highly specialized applications where performance is critical and you want to avoid the overhead of higher-level abstractions. Projects that need to interact with older codebases that rely on _thread.
"""