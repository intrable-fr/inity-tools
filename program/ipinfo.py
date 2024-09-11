import os, requests, sys
from colorama import Fore, Style

class color:
    RED = Fore.RED + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL

def reset_color():
    print(color.RESET)

def ret():
    choice = input(color.WHITE + '[$] Press ENTER to return to the menu: ')
    main()

def error(error):
    print(color.WHITE + '\n[$] Unexpected error in ' + color.RED + 'Api Tracker' + color.WHITE + ': ' + str(error))
    ret()

def exit():
    clear()
    reset_color()
    sys.exit()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_data(data):
    print(color.WHITE + '\n[$] Status: ' + color.RED + data['status'])
    print(color.WHITE + '[$] Continent: ' + color.RED + data['continent'])
    print(color.WHITE + '[$] Country: ' + color.RED + data['country'])
    print(color.WHITE + '[$] Country code: ' + color.RED + data['countryCode'])
    print(color.WHITE + '[$] Region name: ' + color.RED + data['regionName'])
    print(color.WHITE + '[$] City: ' + color.RED + data['city'])
    print(color.WHITE + '[$] Zip: ' + color.RED + str(data.get('zip', '')))
    print(color.WHITE + '[$] Latitude: ' + color.RED + str(data['lat']))
    print(color.WHITE + '[$] Longitude: ' + color.RED + str(data['lon']))
    print(color.WHITE + '[$] Timezone: ' + color.RED + data['timezone'])
    print(color.WHITE + '[$] Currency: ' + color.RED + data['currency'])
    print(color.WHITE + '[$] ISP: ' + color.RED + data['isp'])
    print(color.WHITE + '[$] Organization: ' + color.RED + data['org'])
    print(color.WHITE + '[$] As: ' + color.RED + data['as'])
    print(color.WHITE + '[$] Reverse: ' + color.RED + data['reverse'])
    print(color.WHITE + '[$] Mobile: ' + color.RED + str(data['mobile']))
    print(color.WHITE + '[$] Proxy: ' + color.RED + str(data['proxy']))
    print(color.WHITE + '[$] Hosting: ' + color.RED + str(data['hosting']))
    print(color.WHITE + '[$] IP: ' + color.RED + data['ip'])
    print(color.WHITE + '[$] Cached: ' + color.RED + str(data['cached']))
    print(color.WHITE + '[$] Cache timestamp: ' + color.RED + str(data['cacheTimestamp']) + '\n')

def my_ip():
    try:
        res = requests.get('https://api.ipify.org?format=json')
        public_ip = res.json()['ip']

        res = requests.get(f'https://api.techniknews.net/ipgeo/{public_ip}')
        print_data(data=res.json())

    except Exception as ex:
        error(ex)

    except:
        ret()

    ret()

def other_ip():
    try:
        choice = input(color.WHITE + '\n[$] Enter the public IP address to track: ')

        res = requests.get(f'https://api.techniknews.net/ipgeo/{choice}')
        print_data(data=res.json())

    except Exception as ex:
        error(ex)

    except:
        ret()

    ret()
    
    
    
def back():
        os.system('cls')
        os.system('python Main.py')



def main():
    clear()
    title = '''
╔════════════════════════════════╗  
║ ┬┌─┐  ┬┌┐┌┌─┐┌─┐               ║ 
║ │├─┘  ││││├┤ │ │               ║  
║ ┴┴    ┴┘└┘└  └─┘   by jok3r    ║  
╚════════════════════════════════╝
[0]: quitter le programme
[1]: Avoir les information de votre ip 
[2]: Avoir les information d'une autre adresse ip
[3]: Revenir sur le multitool
'''
    print(color.RED + title)

    choice = input(color.WHITE + '[INPUT] -->  ')

    if choice == '0': exit()
    elif choice == '1': my_ip()
    elif choice == '2': other_ip()
    elif choice == '3': back()
      
    

    else:(error)
main()