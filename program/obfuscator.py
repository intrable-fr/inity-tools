import os
import random
import zlib
import lzma
from marshal import dumps

os.system('cls' if os.name == 'nt' else 'clear')

def purplepink(text):
    os.system("")
    faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

print(purplepink('''
 ██████╗ ██████╗ ███████╗██╗   ██╗███████╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔═══██╗██╔══██╗██╔════╝██║   ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║   ██║██████╔╝█████╗  ██║   ██║███████╗██║     ███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══██╗██╔══╝  ██║   ██║╚════██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝██████╔╝██║     ╚██████╔╝███████║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
 cette obfuscator a etais créer par hash
                                   
'''))

junk = "__skid__" * 15

file = input('Drag and drop your file here : ')

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def genvar():
    var = ''
    for i in range(10):
        var += random.choice(chars)
    return var

def compress(text):
    ok = zlib.compress(text.encode())
    ok = lzma.compress(ok)
    return ok

def encrypt1(text):
    src = compile(text, 'coduter', 'exec')
    ma = dumps(src)
    s = f'{junk}="{junk}";{junk}="{junk}";{junk}="{junk}";exec(loads({ma}));{junk}="{junk}";{junk}="{junk}"'
    compresse = compress(s)
    oke = f"import zlib,lzma\nexec(zlib.decompress(lzma.decompress({compresse})))"
    return oke

def encrypt2(text):
    sta = genvar()
    code = text
    s = compile(code, 'coduter', 'exec')
    maa = dumps(s)
    stub2 = f'from marshal import loads;exec(loads({maa}));'
    fin = f'{junk}="{junk}";{junk}="{junk}";{stub2}{junk}="{junk}";{junk}="{junk}";'
    return fin

if not os.path.isfile(file):
    print('File not found')
    exit()
print('\n')
print('[+] encrypting ...')

# Modifier cette ligne pour utiliser l'encodage utf-8
with open(file, 'r', encoding='utf-8') as f:
    code = f.read()

code = encrypt1(code)
code = encrypt2(code)
print('[+] done')
print('\n')
name = file.split('/')[-1]
name = name.split('.')[0]
with open(f'{name}-obf.py', 'w', encoding='utf-8') as f:
    f.write(code)

os.system('cls' if os.name == 'nt' else 'clear')
print(f'done your file is encrypted and saved as {name}-obf.py')
print('\n')
print('[+] merci d utiliser le tool')
import time
time.sleep(2)
os.system('cls')
os.system("python Main.py")
