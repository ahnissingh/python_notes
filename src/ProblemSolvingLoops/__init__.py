# Leap Year
"""
Leap year are divisible by 4 but not by 100 also divisible by 400
"""


# GPT
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# Mine
year = 2024
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("It is a leap a year")

"-------------------------------LOOOPS------------------------------"


# Q1 Counting Positive Numbers
def positive_numbers():
    numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
    count = 0
    for num in numbers:
        if num >= 0:
            count += 1
    print(count)


def sum_of_evens(n):
    total = 0
    for i in range(0, n + 1, 2):
        total += i
    print(total)


def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")


def reverse_string(string):
    reverse = ""
    for char in string:
        reverse = char + reverse
    return reverse


def non_repeating(string):
    for char in string:
        if string.count(char) == 1:
            return char


def factorial(num):
    fact = 1
    while num >= 1:
        fact *= num
        num -= 1


# O(2^n) O(n)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# O(n) O(1)
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# O(n) O(n) Top Down
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# O(n) O(n)
def fibonacci_bottom_up(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# O(n) O(1)
def fibonacci_space_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def primeNumberChecker(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    else:
        return False
    return True


def prime_number_checker_better(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num ** 0.5) + 1):  # Check divisors up to √num
        if num % i == 0:
            return False  # Found a divisor, not prime
    return True  # No divisors found, it's prime


def prime_number_checker_optimal(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if num <= 3:
        return True  # 2 and 3 are prime numbers
    if num % 2 == 0 or num % 3 == 0:
        return False  # Exclude multiples of 2 and 3

    # Check divisors from 5 to √num, skipping multiples of 2 and 3
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False

    return True


def list_uniqueness(lst):
    unique_item = set()
    for item in lst:
        if item in unique_item:
            return False
        unique_item.add(item)

def is_armstrong_number(num):
    digits = str(num)  # Convert the number to a string to extract digits
    power = len(digits)  # The number of digits determines the power
    total = sum(int(digit) ** power for digit in digits)  # Sum of digits raised to the power
    return total == num  # Check if the sum equals the original number
