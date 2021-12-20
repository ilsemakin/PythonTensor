#!/usr/bin/python3
from math import sqrt

def main():
    """Displays the result of solving a quadratic equation."""
    a = input_number('Enter coefficient A: ')
    b = input_number('Enter coefficient B: ')
    c = input_number('Enter coefficient C: ')

    answer = solve_square_equation(a, b, c)

    if len(answer) == 0:
        print('The equation has no solution!')
    else:
        print('x1 = {:.2f} x2 = {:.2f}'.format(*answer))

def solve_square_equation(a, b, c):
    """Returns the roots of a quadratic equation.
    Parameters
    ----------
    a : int
        Coefficient at x x**2 
    b : int
        Coefficient at x x
    c : int
        Free term
    Returns
    -------
    list
        a list of float roots
    list
        a list of comlex roots
    list
        empty list if there are no roots
    """
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
    """Returns a number.
    Parameters
    ----------
    message : str
        A message to the user when entering data
    
    Returns
    -------
    float
        converted number from string
    """
    while True:
        try:
            number = float(input(message))
        except ValueError:
            print('The input is not a number!\n')
        else:
            return number

if __name__ == '__main__':
    main()