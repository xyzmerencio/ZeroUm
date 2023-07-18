import socket
import sys
import threading


LIMITE_CONEXOES = 100

semafaro = threading.Semaphore(LIMITE_CONEXOES)

def scan_port(host, porta):
    """
    Verifica se uma determinada porta em um host está aberta.

    Args:
        host (str): O endereço IP ou nome do host a ser verificado.
        porta (int): O número da porta a ser verificado.
    """
    try:
        with semafaro:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            code = client.connect_ex((host, porta))
            if code == 0:
                print(f"[+] {porta} aberta")
            client.close()
    except socket.error as error:
        print(error)

def scan(host, porta_espec):
    """
    Executa uma varredura de portas em um host específico.

    Args:
        host (str): O endereço IP ou nome do host a ser varrido.
        porta_espec (str): A especificação das portas a serem varridas. Pode ser um único número de porta,
                           uma lista de portas separadas por vírgula ou um intervalo de portas separado por hífen.

    """
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