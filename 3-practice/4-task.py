#!/usr/bin/python3
import sys
import math

def main():
    a, b, c = [input_number(f'Enter coefficient {coeff}: ') for coeff in ('A', 'B', 'C')]
    answer = solve_square_equation(a, b, c)
    print('x1 = {:.2f} x2 = {:.2f}'.format(*answer))

def solve_square_equation(a, b, c):
    solutions = []

    d = b**2 - 4*a*c

    if d >= 0:
        solutions.append((-b+math.sqrt(d)) / (2*a))
        solutions.append((-b-math.sqrt(d)) / (2*a))
    else:
        solutions.append((-b+complex(0, math.sqrt(-d))) / (2*a))
        solutions.append((-b-complex(0, math.sqrt(-d))) / (2*a))

    return solutions

def input_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print('Input not a number!\n')
            continue
        except KeyboardInterrupt:
            sys.exit('')

main()