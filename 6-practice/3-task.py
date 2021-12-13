#!/usr/bin/python3
from itertools import cycle

def main():
    """Reads a string from a file and encrypts it to another file."""
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    data = read_file(input_file)
    if data is not None:
        key = input('Enter the secret encryption key: ')
        write_file(output_file, xor_shift(key, data))
        
def read_file(name):
    """Reads data from a file.

    Parameters
    ----------
    name : str
        File name to read
    
    Returns
    -------
    str
        string of file data
    None
        if the file is not found
    """
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        print('File not found!')
        return None
    else:
        return data

def write_file(name, data):
    """Writes data to a file.

    Parameters
    ----------
    name : str
        File name to write
    data : str
        Encrypted string for writing
    """
    with open(name, 'w') as file:
        file.write(data)

def xor_shift(key, data):
    """Returns a string encrypted by xor.

    Parameters
    ----------
    key : str
        Cipher key
    data : int
        Original string
    
    Returns
    -------
    str
        encrypted string
    """
    result = ''
    for data_symbol, key_symbol in zip(data, cycle(key)):
        result += chr(ord(data_symbol) ^ ord(key_symbol))
    return result

if __name__ == '__main__':
    main()