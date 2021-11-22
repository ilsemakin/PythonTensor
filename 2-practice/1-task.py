#!/usr/bin/python3
op = ['+', '-', '*', '**', '/', '%', '//']

try:
    num_1 = float(input('Input the first number: '))
    num_2 = float(input('Input the second number: '))

    for i in range(0, len(op)):
        print(f'{ num_1 } { op[i] } { num_2 } = { eval(str(num_1) + op[i] + str(num_2)) }')

except (ValueError):
    print('Error: You input not a number!')
except ZeroDivisionError:
    print('Error: Division by zero!')