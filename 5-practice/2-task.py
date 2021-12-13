#!/usr/bin/python3

def main():
    """Prints the sum of the list of arguments."""
    numbers = input_list("Enter a list of numbers: ")
    print(f'Sum = {all_sum(*numbers)}')

def all_sum(*numbers):
    """Returns the sum of all arguments.
    
    ParametersA message to the user when entering data
    ----------
    numbers : tuple
        Dynamic number of arguments
    
    Returns
    -------
    float
        sum of all arguments
    """

    print(type(numbers))

    result = 0
    for number in numbers:
       result += number         
    return result

def input_list(message):
    """Returns a list of floating point numbers that
    were obtained by converting a list of strings.

    Parameters
    ----------
    message : str
        A message to the user when entering data
    
    Returns
    -------
    list
        a list of float numbers
    """    
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