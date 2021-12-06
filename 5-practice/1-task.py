#!/usr/bin/python3

def main():
    if input_password('Enter password: '):
        print('Good password!')
    else:
        print('Password does not meet requirements!')

def input_password(message):
    black_list = 'password'
    password = input(message)
    
    if len(password) >= 6:
        if password.isdigit() or black_list in password.lower():
            return False
        
        for index in range(len(password)):
            if password[index].isdigit():
                return True     
    else:
        return False

main()