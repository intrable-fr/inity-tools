import socket
from datetime import datetime
import threading
import os
import fade

print(fade.fire("""
                                                   
  

                                                                               
██████╗  ██████╗ ██████╗ ████████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                                                                                                                               

                              PORT CHECKER
                                                       
"""))
      
def get_target():
    hostname = input("Enter your target hostname (or IP address) : ")
    target = socket.gethostbyname(hostname)
    print(f'Scan Target  > {target}')
    return target


def get_port_list():
    print(f'Ports Range  > [1 – 1024]')
    return range(1, 1024)


def scan_port(target, port):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Test connection
        test = s.connect_ex((target, port))
        if test == 0:
            print(f'Port {port} is [open]')


def port_scanner():
    try:
        target = get_target()
        port_list = get_port_list()
        thread_list = list()
        start_time = datetime.now()

        for port in port_list:
            scan = threading.Thread(target=scan_port, args=(target, port))
            thread_list.append(scan)
            scan.daemon = True
            scan.start()

        for scan in thread_list:
            scan.join()
    except:
        print("Something went wrong !")
    else:
        end_time = datetime.now()
        print("Scanning completed in", end_time - start_time)
        print("vous reviendrez au multitool dans 8 seconde.")
        import time
        time.sleep(8)
        os.system('cls')
        os.system('python Main.py')

if __name__ == '__main__':
    port_scanner()