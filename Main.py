import os
import colorama
import subprocess
import webbrowser
import time
import fade
from colorama import Fore , init
ascii_art =  """                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
         ▄█  ███▄▄▄▄    ▄█      ███     ▄██   ▄            ███      ▄██████▄   ▄██████▄   ▄█          ▄████████ 
         ███  ███▀▀▀██▄ ███  ▀█████████▄ ███   ██▄      ▀█████████▄ ███    ███ ███    ███ ███         ███    ███ 
         ███▌ ███   ███ ███▌    ▀███▀▀██ ███▄▄▄███         ▀███▀▀██ ███    ███ ███    ███ ███         ███    █▀  
         ███▌ ███   ███ ███▌     ███   ▀ ▀▀▀▀▀▀███          ███   ▀ ███    ███ ███    ███ ███         ███        
         ███▌ ███   ███ ███▌     ███     ▄██   ███          ███     ███    ███ ███    ███ ███       ▀███████████ 
         ███  ███   ███ ███      ███     ███   ███          ███     ███    ███ ███    ███ ███                ███ 
         ███  ███   ███ ███      ███     ███   ███          ███     ███    ███ ███    ███ ███▌    ▄    ▄█    ███ 
         █▀    ▀█   █▀  █▀      ▄████▀    ▀█████▀          ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██  ▄████████▀  
                                                                                 ▀                         
             ┌─────────────────┐                        ┌───────┐                           ┌───────────┐              
   ┬─────────┤    Network      ├─────────┬──────────────┤ Osint ├──────────────┬────────────┤ Utilities ├─────────────┬
   │         ┘─────────────────┘         │              └───────┘              │            └───────────┘             │ 
   │[01] -> Proxy Scrapper               │ [08] -> Snusbase Search Tools       │ [15] -> Discord Id Info              │ 
   │[02] -> Python obfuscator            │ [09] -> username tracker (osint)    │ [16] -> Join the discord             │ 
   │[03] -> discord id token             │ [10] -> Osint Sites                 │ [17] -> Download Database (menu)     │ 
   │[04] -> Ip Tools                     │ [11] -> Dos Tools                   │ [18] -> Token Bruteforcer            │ 
   │[05] -> Ip Pinger                    │ [12] -> Ip Port Scanner             │ [19] -> discord fake décoration(site)│     
   │[06] -> Webhooks tools               │ [13] -> Database Searcher           │ [20] -> credit                       │ 
   │[07] -> Nitro Generator              │ [14] -> Fivem Scrapper              │ [21] -> soon                         │        
   └─────────────────────────────────────┴─────────────────────────────────────┴──────────────────────────────────────┘                                                                        
""" 


os.system("title made by intrable / .gg/freeforreal")
root = (Fore.MAGENTA + """
┌──(User@InityTools)-[~Menu]│
└─$>"""+Fore.MAGENTA)
ascii_art = fade.purplepink(ascii_art)
print(ascii_art)

choice = input(root)          # ici , j'ai juste preferer mettre un input qu'un print()
if "01" in choice.lower():
    os.system("python checker.py")      # si vous ne comprenez pas pourquoi j'ai fais ca , c juste pour m'aider pour le subprocess                                             



# calculez pas ce que je mets ici mdr

credittool = """
 ██████╗██████╗ ███████╗██████╗ ██╗████████╗
██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝
██║     ██████╔╝█████╗  ██║  ██║██║   ██║   
██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   
╚██████╗██║  ██║███████╗██████╔╝██║   ██║   
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   
[*]Mon discord : intrable
[*]Mon serveur : https://discord.gg/freeforreal
[*]Notez que tout les program sont crédités
[*]Et ne sont pas tous fais par moi
[*]C'est surtout pour aider mon serveur , pour regrouper tout les tools en 1 multitools.
""" 
credittool =  fade.pinkred(credittool)

def options():
    
    commandes = [str(i) for i in range(1, 18)]
    
    
while True:
    gg = choice
    if gg.isdigit():
        gg = int(gg)
    
        
        
    if gg == 1:
        subprocess.run(['python', 'program\\checker.py']) # chaque réponse indiquer ( 1 jusqu'a 18 ) lanceras ducoup le program indiquer
        
        
    elif gg == 2:
        subprocess.run(['python', 'program\\obfuscator.py'])
        
    elif gg == 3:
        subprocess.run(['python', 'program\\idtotoken.py'])
        
    elif gg == 4:
        subprocess.run(['python', 'program\\ipinfo.py'])
        
    elif gg == 5:
        subprocess.run(['python', 'program\\ippinger.py'])
        
    elif gg == 6:
        subprocess.run(['python', 'program\\webhooktool.py'])
    elif gg == 7:
        subprocess.run(['python', 'program\\nitrogen.py'])
        
    elif gg == 8:
        subprocess.run(['python', 'program\\snustool.py'])
        
    elif gg == 9:
        subprocess.run(['python', 'program\\usernametracker.py'])
    
    elif gg == 10:
        subprocess.run(['python', 'program\\osintsites.py'])
        
    elif gg == 11:
        subprocess.run(['python', 'program\\ddos.py'])
        
    elif gg == 12:
        subprocess.run(['python', 'program\\portcheck.py'])
                
    elif gg == 13:
        subprocess.run(['python', 'output\\dbsearcher.py'])
        
    elif gg == 14:
        subprocess.run(['python', 'FivemScrapper\\main.py'])
        
        
    elif gg == 15:
        subprocess.run(['python', 'program\\idinfo.py'])
        
    elif gg == 16:
        webbrowser.open('https://discord.gg/freeforreal')
        os.system('cls')
        os.system('python Main.py')
        
    elif gg == 17:
        subprocess.run(['python', 'program\\database.py'])
        
    elif gg == 18:
        subprocess.run(['python', 'program\\TokenBruteforce.py'])
        
    elif gg == 19:
       webbrowser.open('https://discord-decorations.vercel.app/')
        
    elif gg == 20:
        print(credittool)
        input('appuyer sur entrée pour retourner au multitools : ')
        os.system('cls')
        os.system('python Main.py')

     
 
        
        
        
        
        
    else:
        print('mauvais choix...') 
        time.sleep(1)
        os.system('cls')
        os.system('python Main.py')

 
 
 
 
 
