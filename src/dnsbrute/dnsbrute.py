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
            host = f"{subdominio}.{dominio}"  # Constrói o nome completo do subdomínio
            if len(subdominio) > 0 and len(subdominio) <= MAX:  # Verifica o comprimento do subdomínio
                ip = socket.gethostbyname(host)  # Obtém o endereço IP do subdomínio
                print(f"Subdomínio encontrado: {host} | Endereço IP: {ip}")  # Exibe o subdomínio e o IP associado
        except socket.gaierror:
            # Exceção tratada quando não é possível resolver o nome do host (subdomínio não existe)
            pass
        except IOError:
            # Exceção tratada quando ocorre um erro de I/O ao ler o arquivo de wordlist
            pass

    try:
        with open(wordlist, "r", encoding="utf-8") as arquivo:
            subdominios = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena na lista subdominios

        threads = []
        for subdominio in subdominios:
            subdominio = subdominio.strip()  # Remove espaços em branco e caracteres de quebra de linha
            thread = threading.Thread(target=resolver_subdominio, args=(subdominio,))  # Cria uma thread para resolver o subdomínio
            thread.start()  # Inicia a execução da thread
            threads.append(thread)  # Adiciona a thread à lista de threads criadas

        for thread in threads:
            thread.join()  # Aguarda a conclusão de todas as threads criadas
    except KeyboardInterrupt:
        # Exceção tratada quando o usuário interrompe a execução com Ctrl+C
        print("\n\n\n Tchau :)")  # Exibe uma mensagem de despedida
        sys.exit(0)  # Encerra a execução do programa
