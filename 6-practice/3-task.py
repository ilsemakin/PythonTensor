#!/usr/bin/python3
from itertools import cycle

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    data = read_file(input_file)
    if data is not None:
        key = input('Enter the secret encryption key: ')
        write_file(output_file, xor_shift(key, data))
        
def read_file(name):
    try:
        with open(name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print('File not found!')
        return None

def write_file(name, data):
    with open(name, 'w') as file:
        file.write(data)

def xor_shift(key, data):
    result = ''
    for data_symbol, key_symbol in zip(data, cycle(key)):
        result += chr(ord(data_symbol)^ord(key_symbol))
    return result

main()