import sys
import traceback


def demonstrate_exc_info():
    """
    Demonstrates the use of sys.exc_info() to fetch exception details.
    """
    try:
        1 / 0
    except ZeroDivisionError:
        exc_type, exc_value, exc_tb = sys.exc_info()
        print("--- sys.exc_info() Demonstration ---")
        print(f"Exception Type: {exc_type}")
        print(f"Exception Value: {exc_value}")
        print(f"Traceback Object: {exc_tb}")
        print("------------------------------\n")


def demonstrate_exit():
    """
    Demonstrates the use of sys.exit() to exit a program.
    """
    try:
        print("--- sys.exit() Demonstration ---")
        sys.exit("Exiting program with sys.exit()")
    except SystemExit as e:
        print(f"Caught SystemExit: {e}")
        print("------------------------------\n")


def demonstrate_stderr():
    """
    Demonstrates the use of sys.stderr to write error messages.
    """
    try:
        raise ValueError("An example error written to stderr")
    except ValueError as e:
        print("--- sys.stderr Demonstration ---")
        sys.stderr.write(f"Error: {e}\n")
        print("------------------------------\n")


def demonstrate_tracebacklimit():
    """
    Demonstrates the use of sys.tracebacklimit to control traceback display.
    """
    sys.tracebacklimit = 0  # Suppresses traceback
    print("--- sys.tracebacklimit Demonstration ---")
    try:
        1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError (traceback suppressed)")
    print("------------------------------\n")


def demonstrate_last_attributes():
    """
    Demonstrates the use of sys.last_* attributes to access the last unhandled exception.
    This only works in interactive mode; in scripts, it won't behave as expected.
    """
    print("--- sys.last_* Attributes Demonstration ---")
    try:
        1 / 0
    except ZeroDivisionError:
        pass  # To simulate an unhandled exception in interactive mode

    # These attributes will only show values in interactive mode.
    print("Note: sys.last_* attributes work only in interactive sessions.")
    print("------------------------------\n")

# Demonstrate each feature
if __name__ == "__main__":
    demonstrate_exc_info()
    demonstrate_exit()
    demonstrate_stderr()
    demonstrate_tracebacklimit()
    demonstrate_last_attributes()
