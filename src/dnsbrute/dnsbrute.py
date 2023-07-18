import socket
import sys
import threading

MAX = 63

def dnsbrute(dominio, wordlist):
    """
    Realiza uma busca por subdomínios em um domínio usando uma lista de palavras-chave.
    
    Args:
        dominio (str): O domínio base para a busca.
        wordlist (str): O caminho para o arquivo de lista de palavras-chave.
    """
    def resolver_subdominio(subdominio):
        try:
            host = f"{subdominio}.{dominio}"
            if len(subdominio) > 0 and len(subdominio) <= MAX:
                ip = socket.gethostbyname(host)
                print(f"Subdomínio encontrado: {host} | Endereço IP: {ip}")
        except socket.gaierror:
            pass
        except IOError:
            pass

    try:
        with open(wordlist, "r", encoding="utf-8") as arquivo:
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
