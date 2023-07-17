import socket
import sys
import threading
import time

LIMITE_CONEXOES = 100

semafaro = threading.Semaphore(LIMITE_CONEXOES)

def scan_port(host, porta):
    try:
        with semafaro:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            code = client.connect_ex((host, porta))
            if code == 0:
                print(f"[+] {porta} aberta")
            client.close()
    except Exception as error:
        print(error)

def scan(host, porta_espec):
    try:
        if '-' in porta_espec:
            primeira_porta, ultima_porta = map(int, porta_espec.split('-'))
            porta_list = list(range(primeira_porta, ultima_porta + 1))
        else:
            porta_list = list(map(int, porta_espec.split(',')))

        ip = socket.gethostbyname(host)

        threads = []
        for porta in porta_list:
            thread = threading.Thread(target=scan_port, args=(ip, porta))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\n\n\n Tchau :)")
        sys.exit(0)