import os

osint_site = """

 email : 

https://epieos.com
https://haveibeenpwned.com
https://emailrep.io
__________________________________

 ip : 

https://www.shodan.io
https://ipinfo.io
https://portscanner.online
__________________________________
 visage : 

https://pimeyes.com/en
__________________________________
 nom prenom : 

https://www.pagesjaunes.fr
https://webmii.com
https://www.idcrawl.com
__________________________________
username : 

https://whatsmyname.app
https://www.namecheckr.com
https://usersearch.org
__________________________________
site web osint qui regroupe tout : https://osintframework.com
"""

osint_tools = """
https://github.com/megadose/holehe
__________________________________
https://github.com/p1ngul1n0/blackbird
__________________________________
https://github.com/N0rz3/Zehef
__________________________________
https://github.com/sherlock-project/sherlock
"""


print(osint_site)


print(osint_tools)


question = " voulez vous re aller au menu principal ? appuyer sur la touche 0 pour revenir au menu : "

reponse = input(question)
if "0" in reponse.lower():
    os.system('cls')
    os.system('python Main.py')