import random, string, requests, sys, os
from os import system as cmd
from time import sleep as wait
from colorama import Fore, Style

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class color:
    RED = Fore.RED + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL

amount = 0

def make_code(length=19):
    characters = string.ascii_uppercase + string.digits
    nitro_code = ''.join(random.choice(characters) for _ in range(length))
    return nitro_code

def check_code(code):
    valid = requests.get(f'https://discord.com/api/v9/entitlements/gift-codes/{code}')

    if not valid.status_code == 200:
        return False
    else:
        return True

title = '''
          $$\   $$\                                                       
          \__|  $$ |                                                      
$$$$$$$\  $$\ $$$$$$\    $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\  
$$  __$$\ $$ |\_$$  _|  $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |  $$ |$$ |  $$ |    $$ |  \__|$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |$$\ $$ |      $$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |
$$ |  $$ |$$ |  \$$$$  |$$ |      \$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |
\__|  \__|\__|   \____/ \__|       \______/  \____$$ | \_______|\__|  \__|
                                            $$\   $$ |                    
                                            \$$$$$$  |                    
                                             \______/                    
'''

while not amount >= 1:
    clear()
    print(Fore.RED + title)

    amount = input(color.WHITE + '[$] Enter the amount of codes to generate: ')

    try:
        amount = int(amount)

        if amount <= 0:
            print(color.RED + '\n[$] Error: Please write a valid number')
            input()
            print(color.RESET)
            sys.exit()

    except ValueError:
        print(color.RED + '[$] Error: Please write a valid number')
        input()
        print(color.RESET)
        sys.exit()

print('\n')

with open('nitro-codes.txt', 'w') as file:
    for i in range(amount):
        code = make_code()

        valid = check_code(code)

        if valid:
            print(color.WHITE + f'[$] Valid Nitro code mined: {color.RED}{code}{color.WHITE} in attempt [{color.RED}{i + 1}{color.WHITE}]')
            file.write(f'{code} - VALID\n')
        else:
            print(color.RED + f'[$] Invalid Nitro code mined: {color.WHITE}{code}{color.RED} in attempt [{color.WHITE}{i + 1}{color.RED}]')
            file.write(f'{code} - INVALID\n')

print(color.WHITE + '\n[$] Generation end')
input()
print(color.RESET)
os.system('cls')
os.system('python Main.py')