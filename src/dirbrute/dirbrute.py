import sys
import concurrent.futures
from requests.exceptions import RequestException
import requests

def dirbrute(url, wordlist):
    """
    Realiza uma busca por diretórios em uma URL usando uma lista de palavras-chave.
    
    Args:
        url (str): A URL base para a busca.
        wordlist (list): Uma lista de palavras-chave para a busca.
    """
    def check_url(word):
        # Remove espaços em branco do início e final da palavra
        word = word.strip()
        # Cria a URL final acrescentando a palavra da wordlist à URL base
        url_final = f"{url}/{word}"
        try:
            # Faz a requisição HTTP para a URL formada com a palavra da wordlist
            response = requests.get(url_final, timeout=5)
            # Verifica se o status code da resposta não é 404 (não encontrado)
            if response.status_code != 404:
                # Se o status code não for 404, imprime a URL encontrada e o status code
                print(url_final, response.status_code)
        except RequestException as error:
            # Trata exceções relacionadas a problemas com a requisição (exemplo: timeout, erro de conexão)
            print(error)

    # Cria um pool de threads usando o contexto "concurrent.futures.ThreadPoolExecutor()"
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Mapeia a função "check_url" para cada palavra da "wordlist"
        # Isso permite que as requisições sejam feitas em paralelo, utilizando threads
        executor.map(check_url, wordlist)
