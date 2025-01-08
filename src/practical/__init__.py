def reverse_words(inputString: str) -> str:
    words = inputString.split()
    reversedWords = words[::-1]
    return ' '.join(reversedWords)


def power(self, x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / self.power(x, -n)

    half_power = self.power(x, n // 2)
    if n % 2 == 0:
        return half_power * half_power
    else:
        return x * half_power * half_power


def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    total: int = 0
    for digit in num_str:
        total += int(digit) ** num_len

    return total == num


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def fibbonaci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def int_to_roman(num):
    roman_map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'Xl',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman = []
    for value in sorted(roman_map.keys(), reverse=True):
        while num >= value:
            roman.append((roman_map[value]))
            num -= value
    return ' '.join(roman)
