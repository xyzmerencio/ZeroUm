import socket
import sys
import threading

MAX = 63

def dnsbrute(dominio, wordlist):
    def resolver_subdominio(subdominio):
        try:
            host = f"{subdominio}.{dominio}"
            if len(subdominio) > 0 and len(subdominio) <= MAX:
                ip = socket.gethostbyname(host)
                print(f"Subdomínio encontrado: {host} | Endereço IP: {ip}")
        except socket.gaierror:
            pass
        except Exception as error:
            pass

    try:
        with open(wordlist, "r") as arquivo:
            subdominios = arquivo.readlines()

        threads = []
        for subdominio in subdominios:
            subdominio = subdominio.strip()
            thread = threading.Thread(target=resolver_subdominio, args=(subdominio,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\n\n\n Tchau :)")
        sys.exit(0)
