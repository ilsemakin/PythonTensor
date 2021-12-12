#!/usr/bin/python3
operations = ['+', '-', '*', '**', '/', '%', '//']

try:
    num_1 = float(input('Input the first number: '))
    num_2 = float(input('Input the second number: '))

    for operation in operations:
        result = eval(str(num_1) + operation + str(num_2))
        print(f'{num_1} {operation} {num_2} = {result}')

except ValueError:
    print('Error: You input not a number!')
except ZeroDivisionError:
    print('Error: Division by zero!')