#!/usr/bin/python3

def main():
    encoded_strings = encode_list(input_list('Enter a list of strings: '))
    decoded_strings = decode_list(encoded_strings)

    print(f'Encoded strings: {encoded_strings}')
    print(f'Decoded strings: {decoded_strings}')

encode_list = lambda strings: [string.encode('utf-8') for string in strings]
decode_list = lambda strings: [string.decode('utf-8') for string in strings]
input_list = lambda message: input(message).split(' ')

main()