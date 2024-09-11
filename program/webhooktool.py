import requests
import time
import pystyle
import os
import json
from pystyle import Colors, Colorate

def send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url=None):
    payload = {
        'username': username,
        'content': message,
        'avatar_url': avatar_url
    }
    print(Colorate.Horizontal(Colors.red_to_yellow, """
    Spamming..."""))

    for _ in range(num_messages):
        requests.post(webhook_url, json=payload)
        time.sleep(cooldown)

    print(Colorate.Horizontal(Colors.red_to_yellow, """
    Spamming done."""))

def delete_webhook(webhook_url):
    requests.delete(webhook_url)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_webhook_info(webhook_url):
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            webhook_data = response.json()
            print(Colorate.Horizontal(Colors.red_to_yellow, "Webhook Information:"))
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Webhook Name: {webhook_data['name']}"))
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Created by: {webhook_data['user']['username']}"))

            # Check if the webhook provides server (guild) and channel information
            if 'guild_id' in webhook_data and 'channel_id' in webhook_data:
                guild_id = webhook_data['guild_id']
                channel_id = webhook_data['channel_id']
                print(Colorate.Horizontal(Colors.red_to_yellow, f"Server ID : {guild_id}"))
                print(Colorate.Horizontal(Colors.red_to_yellow, f"Channel ID: {channel_id}"))
            else:
                print(Colorate.Horizontal(Colors.red_to_yellow, "Server and Channel information not available."))
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Unable to retrieve webhook information. Make sure the URL is correct."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_yellow, f"An error occurred: {str(e)}"))

def return_to_menu():
    input(Colorate.Horizontal(Colors.red_to_yellow, "\nPress Enter to return to the menu."))
    clear_console()
    show_menu()

def exit_program():
    clear_console()
    print(Colorate.Horizontal(Colors.red_to_yellow, "Exiting the program."))
    exit()

def show_menu():
    clear_console()
    print(Colorate.Horizontal(Colors.red_to_yellow, """
 ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     
 ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
 ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝        ██║   ██║   ██║██║   ██║██║     
 ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗        ██║   ██║   ██║██║   ██║██║     
 ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗       ██║   ╚██████╔╝╚██████╔╝███████╗
  ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                               
                                 by nyxoy.xyz
"""))

    menu_choice = input(Colorate.Horizontal(Colors.red_to_yellow, """
                                 [1] Spam the webhook
                                 [2] Delete the webhook
                                 [3] Webhook information
                                 [4] Back to Multitool
                                 
  Enter your choice: """))

    if menu_choice == "1":
        webhook_url = input(Colorate.Horizontal(Colors.red_to_yellow, "Webhook URL: "))
        username = input(Colorate.Horizontal(Colors.red_to_yellow, "Webhook Name: "))
        message = input(Colorate.Horizontal(Colors.red_to_yellow, "Message: "))
        num_messages = int(input(Colorate.Horizontal(Colors.red_to_yellow, "How many messages: ")))
        cooldown = int(input(Colorate.Horizontal(Colors.red_to_yellow, "Cooldown (0 = no cooldown): ")))
        avatar_url = input(Colorate.Horizontal(Colors.red_to_yellow, "Avatar link: "))

        send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url)
        return_to_menu()

    elif menu_choice == "2":
        webhook_url = input(Colorate.Horizontal(Colors.red_to_yellow, "Webhook URL: "))
        delete_webhook(webhook_url)
        print(Colorate.Horizontal(Colors.red_to_yellow, "Webhook deleted."))
        return_to_menu()

    elif menu_choice == "3":
        webhook_url = input(Colorate.Horizontal(Colors.red_to_yellow, "Webhook URL: "))
        get_webhook_info(webhook_url)
        return_to_menu()

    elif menu_choice == "4":
        os.system('cls')
        os.system('python Main.py')

    else:
        print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid choice."))
        return_to_menu()

# Start the program
show_menu()
