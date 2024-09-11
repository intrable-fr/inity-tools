import requests
import os

sites = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Tiktok": "https://www.tiktok.com/search/user?q={}"
}

def check_username(username):
    available_sites = []
    for site, url in sites.items():
        check_url = url.format(username)
        response = requests.get(check_url)
        if response.status_code == 200:
            available_sites.append(site)
            print(f"[+] {username} trouvé sur {site} : {check_url}")
        else:
            print(f"[-] {username} non trouvé sur {site}")

    if not available_sites:
        print(f"\nLe pseudo'{username}' n'a pas etais trouver sur les site ")
    else:
        print(f"\nLe Pseudo  '{username}' a etais trouvé sur les site suivants : {', '.join(available_sites)}")


if __name__ == "__main__":
    username_to_check = input("Entrez le nom d'utilisateur à vérifier : ")
    check_username(username_to_check)

finish = " check terminé !! ecris 0 pour retourner au multitool ! "


reponse=input(finish)
if "0" in reponse.lower():
        os.system('cls')
        os.system('python Main.py')