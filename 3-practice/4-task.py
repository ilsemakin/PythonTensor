#!/usr/bin/python3
from math import sqrt

def main():
    a = input_number(f'Enter coefficient A: ')
    b = input_number(f'Enter coefficient B: ')
    c = input_number(f'Enter coefficient C: ')
    
    answer = solve_square_equation(a, b, c)

    if len(answer) == 0:
        print('The equation has no solution!')
    else:
        print('x1 = {:.2f} x2 = {:.2f}'.format(*answer))

def solve_square_equation(a, b, c):
    solutions = []

    d = b**2 - 4*a*c
    try:
        if d >= 0:
            solutions.append((-b+sqrt(d)) / (2*a))
            solutions.append((-b-sqrt(d)) / (2*a))
        else:
            solutions.append((-b+complex(0, sqrt(-d))) / (2*a))
            solutions.append((-b-complex(0, sqrt(-d))) / (2*a))
    except ZeroDivisionError:
        print('Error: Division by zero!')
    
    return solutions

def input_number(message):
    while True:
        try:
            number = float(input(message))
        except ValueError:
            print('The input is not a number!\n')
        else:
            return number

if __name__ == '__main__':
    main()