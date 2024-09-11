import requests, os

def clear():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

API_URL = 'https://discordlookup.mesalytic.moe/v1/user/'

def main():
    clear()
    user = int(input('Enter the user ID to gather information: '))
    try:
        response = requests.get(API_URL + str(user))

        if response.status_code == 200:
            data = response.json()
                
            def format_user_info(data, indent=0):
                info = []
                for key, value in data.items():
                    if isinstance(value, dict):
                        info.append("  " * indent + f"{key.replace('_', ' ').title()}:")
                        info.append(format_user_info(value, indent + 1))
                    else:
                        if isinstance(value, list):
                            value = ", ".join(str(v) for v in value)
                        info.append("  " * indent + f"{key.replace('_', ' ').title()}: {value}")
                return '\n'.join(info)
                
            user_info = format_user_info(data)
            print('\n-------------------------------------------------------------------------------')
            print(user_info)
            print('\n-------------------------------------------------------------------------------')
            
            input('appuyer sur entrée pour revenir au multitool...')+os.system('cls + python Main.py')
            
            
                
                      
        input()
        main()

    except Exception as ex:
        print('Error: ' + str(ex))


if __name__ == '__main__':
    main()