#!/usr/bin/python3
from functools import lru_cache

def main():
    number = input_number('Enter the number: ')
    print(f'Fibonacci number = {fibonacci(number)}')

@lru_cache()
def fibonacci(number):
    if number in (1, 2):
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)


def input_number(mesage):
    while True:
        try:
            number = float(input(mesage))
            if number <= 0:
                raise ValueError
        except ValueError:
            print('Input is not a positive number!\n')
        else:
            return number

if __name__ == '__main__':
    main()