import os
import time
import json
import uuid
import requests
import re
from fake_useragent import UserAgent
from pystyle import Colors, Colorate

def clean_filename(hostname):
    """Clean the hostname to be a valid filename."""
    return re.sub(r'[0-9]', '', re.sub(r'[/:"*?<>|]', '', hostname))

def check_if_player_exists(filename, player_data, added_players):
    """Check if a player already exists in the file."""
    if player_data['identifiers'] in added_players:
        return True

    if not os.path.exists(filename):
        return False

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    existing_player = json.loads(line)
                    if existing_player.get('fivem') == player_data.get('fivem'):
                        fields_to_check = ['steam', 'name', 'live', 'xbl', 'license', 'license2']
                        if all(existing_player.get(field) == player_data.get(field) for field in fields_to_check):
                            return True
                except json.JSONDecodeError:
                    continue

        return False

    except Exception as e:
        print(Colorate.Horizontal(Colors.purple_to_red, f"Error checking player existence: {str(e)}"))
        return False

def get_server_info(server_id, proxy, added_players):
    """Retrieve server information and save player data."""
    url = f'https://servers-frontend.fivem.net/api/servers/single/{server_id}'
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random}

    try:
        response = requests.get(url, headers=headers, proxies=proxy, timeout=10)

        if response.status_code == 200:
            server_data = response.json()
            hostname = clean_filename(str(uuid.uuid4()))

            try:
                hostname = clean_filename(server_data['Data']['hostname'])[:100]
            except KeyError:
                pass

            try:
                project_name = server_data['Data']['vars']['sv_projectName']
                if len(project_name) >= 10:
                    hostname = clean_filename(project_name)[:100]
            except KeyError:
                pass

            if not os.path.exists('dump'):
                os.makedirs('dump')

            filename = f'dump/{hostname}.txt'

            for player in server_data['Data']['players']:
                if not check_if_player_exists(filename, player, added_players):
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(json.dumps(player, ensure_ascii=False) + '\n')

                    print(Colorate.Horizontal(Colors.purple_to_red, f'[NEW] {player["name"]} a été ajouté !'))
                    added_players.append(player['identifiers'])

            print(Colorate.Vertical(Colors.purple_to_red, f'\n[INFO] Serveur id : {server_id}'))

        else:
            print(Colorate.Vertical(Colors.purple_to_red, f'\n[INFO] Made By Cristal\n[ERROR] Message d\'erreur ({server_id}: {response.status_code})\n'))

    except requests.RequestException as e:
        print(Colorate.Horizontal(Colors.purple_to_red, f'Error fetching server info: {str(e)}'))

def process_servers(server_ids, proxies, added_players):
    """Process each server ID with corresponding proxy."""
    for server_id, proxy in zip(server_ids, proxies):
        get_server_info(server_id, proxy, added_players)
        time.sleep(0.5)

def load_file_lines(filename):
    """Load lines from a file and strip whitespace."""
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(Colorate.Horizontal(Colors.purple_to_red, f"File {filename} not found."))
        return []

def main():
    french_server_ids = load_file_lines('serveur.txt')
    proxy_list = [{'http': f'socks5://{proxy}'} for proxy in load_file_lines('proxy.txt')]
    added_players = []

    while True:
        process_servers(french_server_ids, proxy_list, added_players)

def startup():
    os.system("cls" if os.name == "nt" else "clear")
    banner = '''
    
    
    
   ▄████████  ▄████████    ▄████████    ▄████████    ▄███████▄    ▄███████▄    ▄████████    ▄████████ 
  ███    ███ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
  ███    █▀  ███    █▀    ███    ███   ███    ███   ███    ███   ███    ███   ███    █▀    ███    ███ 
  ███        ███         ▄███▄▄▄▄██▀   ███    ███   ███    ███   ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀███████████ ███        ▀▀███▀▀▀▀▀   ▀███████████ ▀█████████▀  ▀█████████▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
         ███ ███    █▄  ▀███████████   ███    ███   ███          ███          ███    █▄  ▀███████████ 
   ▄█    ███ ███    ███   ███    ███   ███    ███   ███          ███          ███    ███   ███    ███ 
 ▄████████▀  ████████▀    ███    ███   ███    █▀   ▄████▀       ▄████▀        ██████████   ███    ███ 
                          ███    ███                                                       ███    ███                                  
                                                                            
    

                                               
'''
    print(Colorate.Vertical(Colors.purple_to_red, banner))
    time.sleep(1)
    main()

startup()
