import os
import webbrowser
import fade
import subprocess



database_all = """
██████╗  █████╗ ████████╗ █████╗ ██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
██║  ██║███████║   ██║   ███████║██████╔╝███████║███████╗█████╗  cela vous amenera vers votre naviguateur
██║  ██║██╔══██║   ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══╝  
██████╔╝██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║███████║███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│[01] -> Credit                         │
│[02] -> NazApi                         │ 
│[03] -> Fivem (2024)                   │ 
│[04] -> Minecraft                      │       
│[05] -> Discord                        │                                
│[06] -> Prevname                       │                                
│[07] -> paypal                         │                                
│[08] -> Snapchat                       │                                
│[09] -> Gmod                           │                               
│[10] -> Valorant                       │                                
│[11] -> Orange                         │                                
│[12] -> Instagram                      │                            
│[13] -> Doxbin                         │       
│[14] -> Retourner Au Multitool         │
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
"""

database_all = fade.pinkred(database_all)

choice = "entrée votre choix : "
print(database_all)



choice = input(choice)
if "01" in choice.lower():
    os.system("python checker.py")  
    
def options():
    
    commandes = [str(i) for i in range(1, 13)]
    
    
while True:
    gg = choice
    if gg.isdigit():
        gg = int(gg)
        
        
    if gg == 1:
     subprocess.run(['python', 'program\\credit.py'])
        
    elif gg == 2:
        webbrowser.open('https://mega.nz/file/trFkXIAY#sUM3Fi0L9QkshiY0uKc_nhUIkbyJ58qix3OaqcZjSlI')
        os.system('cls')
        os.system('python Main.py')   
      
    elif gg == 3:
        webbrowser.open('https://cdn.discordapp.com/attachments/1278899112674332804/1279081742032044175/pack_fivem_2K24__2K23_by_intrable.zip?ex=66d670f3&is=66d51f73&hm=e6cf3c79f0efaaa10f9c43f69fd0bb7cd6691f67f02285c5644c4d4943bbf2bc&')
        os.system('cls')
        os.system('python Main.py') 
        
    elif gg == 4:
        webbrowser.open('https://gofile.io/d/EggYGD')
        os.system('cls')
        os.system('python Main.py')  
        
        
    elif gg == 5:
        webbrowser.open('https://gofile.io/d/rXKCqi')
        os.system('cls')
        os.system('python Main.py')
        
    
    elif gg == 6:
        webbrowser.open('https://cdn.discordapp.com/attachments/1273442807893458985/1276863452211580969/Prevname.rar?ex=66d64801&is=66d4f681&hm=59892a6f962cd8432fc83e4e6261c2307e6487fb458f3b789a886a9de351b621&')
        os.system('cls')
        os.system('python Main.py')   
        
    elif gg == 7:
        webbrowser.open('https://cdn.discordapp.com/attachments/1265006757395042324/1265007167191388170/Paypal.txt?ex=66d6a77b&is=66d555fb&hm=fb4dfca30150e56b5d357c48cfb6afe0e8e955b59a31615f6704f900ebee7dfa&')
        webbrowser.open('https://cdn.discordapp.com/attachments/1265006757395042324/1265007168654938173/Paypal1.txt?ex=66d6a77b&is=66d555fb&hm=79de447a1e7765395c3276a1e4e77aa6913c78d235c7be9b4f97b516df495db5&')
        webbrowser.open('https://cdn.discordapp.com/attachments/1265006757395042324/1265007163521368206/DB_PAYPAL_2024.txt?ex=66d6a77a&is=66d555fa&hm=e2941e31a010672774f467379aa464f6678cbd2990e51ebf0332ec90be5a4932&')
        os.system('cls')
        os.system('python Main.py')   
        
    elif gg == 8:
        webbrowser.open('https://gofile.io/d/QzYzDt')
        os.system('cls')
        os.system('python Main.py') 
    
    elif gg == 9:
        webbrowser.open('https://cdn.discordapp.com/attachments/1265101328401567785/1265101361054220330/gmodlife_bots.txt?ex=66d65674&is=66d504f4&hm=72fb076b0af0d668ea757bbd827346b0a154a7441a4c103629ae12f5e4bf290e&')
        webbrowser.open('https://cdn.discordapp.com/attachments/1265101328401567785/1265101361523986614/payment_gmod_life.txt?ex=66d65675&is=66d504f5&hm=651ffceec98246af617a3583c91ac55302dea6a3475d650549def5ae2277cc14&')
        webbrowser.open('https://cdn.discordapp.com/attachments/1265101328401567785/1265101360592982107/email_gmod_life.txt?ex=66d65674&is=66d504f4&hm=85eccebb586e4ad9ee4697d658a0f052b835298035c166641c78b8572935a698&')
        os.system('cls')
        os.system('python Main.py') 
        
       
    elif gg == 10:
        webbrowser.open('https://cdn.discordapp.com/attachments/1265008463134588948/1265008572371042346/4.6k_Valorant_Account.txt?ex=66d6a8ca&is=66d5574a&hm=e9e4a909c56ad97ce035ebd67da45bd5b211a5ea42978aba00b69b8c2841c8f3&')
        webbrowser.open('https://cdn.discordapp.com/attachments/1257370243253141525/1258323888841035796/DB_Valorant.rar?ex=66d6baf1&is=66d56971&hm=185a71406da7a0ba303b107b4e51a453a1472920d21ac28b7160fecd0097b4b9&')
        os.system('cls')
        os.system('python Main.py')  
        
    elif gg == 11:
        webbrowser.open('https://cdn.discordapp.com/attachments/1265008280586158090/1265009783547887796/orange-wanadoo1.txt?ex=66d6a9eb&is=66d5586b&hm=defed2c4ef8b2d278da7cba37a29c720a9d6bbc4cf533b17a0f623789954957d&')
        webbrowser.open('https://cdn.discordapp.com/attachments/1265008280586158090/1265009783094775869/754K_HQ_FRANCE_DATABASE_ORANGE_WANADOO.txt?ex=66d6a9eb&is=66d5586b&hm=d3d1eb9da1d88cc42b9b34fb00cc155a993cdd5c9aa6b918ae567b67c4f48f97&')
        webbrowser.open('https://cdn.discordapp.com/attachments/1265008280586158090/1265009781832159374/120k_orange.txt?ex=66d6a9ea&is=66d5586a&hm=3dea8d95a6f84444afc0b18b5ff72fd56399e77172d91726558608d86dc4933d&')
        os.system('cls')
        os.system('python Main.py')
        
    elif gg == 12:
        webbrowser.open('https://gofile.io/d/cpVHO3')
        webbrowser.open('https://cdn.discordapp.com/attachments/1265008565974859887/1265012631538765945/instagram.txt?ex=66d6ac92&is=66d55b12&hm=037f3e701c4949698da274fa36e4c3b44d70ca3fe07d2af261ef7e967a6b3fca&')
        os.system('cls')
        os.system('python Main.py')
        
        
    elif gg == 13:
        webbrowser.open('https://gofile.io/d/jQQkKW')
        os.system('cls')
        os.system('python Main.py')    
        
        
    elif gg == 14:
        os.system('cls')
        os.system('python Main.py')
        
        
        
    
    
else:
    print('error')
    os.system('cls')
    os.system('python database.py')