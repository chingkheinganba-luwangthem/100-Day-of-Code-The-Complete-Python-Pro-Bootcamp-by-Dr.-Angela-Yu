import os

def clear():
    # Check if the operating system is Windows
    if os.name == 'nt':
        # For Windows
        os.system('cls')
    else:
        # For Linux and Mac
        os.system('clear')
