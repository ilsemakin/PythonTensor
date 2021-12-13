#!/usr/bin/python3
from functools import lru_cache

def main():
    """Prints the Fibonacci number."""
    number = input_number('Enter the number: ')
    print(f'Fibonacci number = {fibonacci(number)}')

@lru_cache()
def fibonacci(number):
    """Returns the Fibonacci number.

    Parameters
    ----------
    number : int
        Fibonacci number ordinal
    
    Returns
    -------
    self recursively
        if the sequence number is not 1 or 2
    1
        otherwise
    """
    if number in (1, 2):
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)


def input_number(mesage):
    """Returns a positive integer number.

    Parameters
    ----------
    message : str
        A message to the user when entering data
    
    Returns
    -------
    int
        converted number from string
    """
    while True:
        try:
            number = int(input(mesage))
            if number <= 0:
                raise ValueError
        except ValueError:
            print('The input is not a positive integer number!\n')
        else:
            return number

if __name__ == '__main__':
    main()