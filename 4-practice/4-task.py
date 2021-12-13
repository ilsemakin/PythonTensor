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
    """Prints help and processes user commands."""
    print_help()
    while True:
        commands[input_comand('Enter the command number: ')]()
        print('\n')

def input_comand(message):
    """Returns the correct command number.

    Parameters
    ----------
    message : str
        A message to the user when entering data

    Returns
    -------
    int
        command number
    """
    while True:
        command_key = input(message)
        try:
            if command_key not in ('0', '1', '2', '3', '100'):
                raise KeyError
        except KeyError:
            print('Command not found!\n')
        else:
            return int(command_key)

def add_item():
    """Adds an inventory item to the list."""
    item = input_item('Enter item: ')

    if item:
        if check_weight(item[1]):
            inventory[item[0]] = item[1]
            print(f'Item <{item[0]}> added to inventory!')
        else:
            print('Inventory full!')
    
def check_weight(item_weight):
    """Checks the weight of the inventory.
    
    Parameters
    ----------
    item_weight : int
        Weight of the item being checked

    Returns
    -------
    True
        true if the item can be put into inventory
    False
        false if inventory is full
    """
    checksum = item_weight
    for key in inventory:
        checksum += inventory[key]
    
    if checksum <= MAX_WEIGHT:
        return True
    else:
        return False

def remove_item():
    """Removes an item from inventory."""
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
    """Prints all inventory items."""
    if len(inventory) != 0:
        for key, value in inventory.items():
            print(f'{key} - {value}')
    else:
        print('Inventory is empty!')

def print_help():
    """Prints help for the user."""
    for command_num, description in reference.items():
        print(f'{command_num} -> {description}')        

def input_item(message):
    """Returns the name of the item with the correct weight.

    Parameters
    ----------
    message : str
        A message to the user when entering data

    Returns
    -------
    list
        a list with item and weight in the format [item name, weight]
    list
        empty list if data is invalid
    """
    item = input(message).split(' ')
    if len(item) == 2:
        try:
            item[1] = float(item[1])
            if item[1] <= 0:
                raise ValueError
        except ValueError:
            print('The input is not a positive number!')
        else:
            return item
    else:
        print('Invalid number of parameters!')

    return []

def finish():
    """Ends the program."""
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