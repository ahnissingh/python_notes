class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def _multiply(x, y):  # _multiply is a "private" method
        return x * y

    @staticmethod
    def _divide(x, y, floor=True):  # _divide is a "private" method
        if y == 0:
            raise ZeroDivisionError("Division by Zero")
        return x // y if floor else x / y
