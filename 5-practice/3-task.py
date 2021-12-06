#!/usr/bin/python3
from functools import lru_cache

def main():
    print(f'Fibonacci number = {fibonacci(input_number("Enter the number: "))}')

@lru_cache()
def fibonacci(number):
    if number in (1, 2):
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2) 

def input_number(mesage):
    while True:
        try:
            return float(input(mesage))
        except ValueError:
            print('Input not a number!\n')

main()