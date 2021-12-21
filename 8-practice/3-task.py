#!/usr/bin/python3
from itertools import cycle
import time

def log(func):
    def wrapper(*args):
        with open('log.txt', 'w') as f:
            f.write(f'Beginning:\t{time.asctime()}\n')
            result = func(*args)
            f.write(f'Ending:\t\t{time.asctime()}')
            return result
    return wrapper

def stopwatch(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f'{end - start} sec\n')
        return result
    return wrapper

def deceleration(sec):
    def decorator(func):
        def wrapper(*args):
            time.sleep(sec)
            return func(*args)
        return wrapper
    return decorator

@log
@stopwatch
@deceleration(3)
def xor_shift(key, data):
    """Returns a string encrypted by xor.

    Parameters
    ----------
    key : str
        Cipher key
    data : int
        Original string
    
    Returns
    -------
    str
        encrypted string
    """
    result = ''
    for data_symbol, key_symbol in zip(data, cycle(key)):
        result += chr(ord(data_symbol) ^ ord(key_symbol))
    return result


cipher = xor_shift('123', 'Hello, Tensor!')
print(f'Encrypted string: {cipher}')