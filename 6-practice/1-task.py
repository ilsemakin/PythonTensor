#!/usr/bin/python3

def main():
    encoded_strings = encode_list(input_list('Enter a list of strings: '))
    decoded_strings = decode_list(encoded_strings)

    print(f'Encoded strings: {encoded_strings}')
    print(f'Decoded strings: {decoded_strings}')

def encode_list(strings):
    return [tuple(ord(symbol) for symbol in string) for string in strings]

def decode_list(strings):
    return [''.join([chr(code) for code in string]) for string in strings]

def input_list(message):
    return [string for string in input(message).split(' ') if string]

if __name__ == '__main__':
    main()