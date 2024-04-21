def add(val_1, val_2):
    return val_1 + val_2


def subtract(val_1, val_2):
    return val_1 - val_2


def multiply(val_1, val_2):
    return val_1 * val_2


def divide(val_1, val_2):
    if val_2 == 0 or val_2 == '':
        return 0
    else:
        return val_1 / val_2

