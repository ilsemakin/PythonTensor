#!/usr/bin/python3

def main():
    numbers = input_list("Enter a list of numbers: ")
    print(f'Sum = {all_sum(*numbers)}')

def all_sum(*numbers):
    result = 0
    for number in numbers:
       result += number         
    return result

def input_list(message):
    while True:
        numbers = input(message)
        
        if len(numbers) == 0:
            return numbers
        else:
            numbers = numbers.split(' ') 

        try:
            for index, number in enumerate(numbers):
                numbers[index] = float(number)
        except ValueError:
            print('Input not a number!\n')
        else:
            return numbers

if __name__ == '__main__':
    main()