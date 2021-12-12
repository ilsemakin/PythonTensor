#!/usr/bin/python3
MAX_WEIGHT = 100

reference = {
    0: 'Print help',
    1: 'Add a new item to inventory',
    2: 'Remove item from inventory',
    3: 'Print inventory',
    100: 'Exit the program'
}

inventory = {}

def main():
    print_help()
    while True:
        commands[input_comand('Enter the command number: ')]()
        print('\n')

def input_comand(message):
    while True:
        try:
            command_key = input(message)
            
            if command_key.isdigit():
                command_key = int(command_key)
                commands[command_key]
            else:
                raise KeyError
        except KeyError:
            print('Command not found!\n')
        else:
            return command_key

def add_item():
    item = input_item('Enter item: ')
    if item != None:
        if check_weight(item[1]):
            inventory[item[0]] = item[1]
            print(f'Item <{item[0]}> added to inventory!')
        else:
            print('Inventory full!')
    
def check_weight(item_weight):
    checksum = item_weight
    for key in inventory:
        checksum += inventory[key]
    
    if checksum <= MAX_WEIGHT:
        return True
    else:
        return False

def remove_item():
    if len(inventory) != 0:
        inventory_key = input('Enter the item to delete from inventory: ')
        try:
            inventory.pop(inventory_key)
        except KeyError:
            print('Item not found!')
        else:
            print(f'Item <{inventory_key}> deleted!')
    else:
        print('Inventory is empty!')
    
def print_items():
    if len(inventory) != 0:
        for key, value in inventory.items():
            print(f'{key} - {value}')
    else:
        print('Inventory is empty!')

def print_help():
    for command_num, description in reference.items():
        print(f'{command_num} -> {description}')        

def input_item(message):
    item = input(message).split(' ')
    if len(item) == 2:
        try:
            item[1] = float(item[1])
        except ValueError:
            print('The input is not a number!')
        else:
            return item
    else:
        print('Invalid number of parameters!')

def finish():
    exit()

commands = {
    0: print_help,
    1: add_item, 
    2: remove_item,
    3: print_items,
    100: finish
}

if __name__ == '__main__':
    main()