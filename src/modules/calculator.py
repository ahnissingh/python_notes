print('Welcome to calculator module ..... it\'s being loaded')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    if x == 0 or y == 0: return 0
    return x * y


def divide(x, y, floor=True):
    if y == 0:
        raise ZeroDivisionError("Division by Zero")
    elif x == 0:
        return 0
    return x // y if floor == True else x / y


__all__ = ['add', 'subtract']
# if __name__ != 'main':
#     raise ImportError(" HEHE You can't huh import this lmao")
# # print('module is done loading')
# else:
#     print('Module is being run directly')
