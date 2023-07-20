import sys
from requests.exceptions import RequestException
import requests


def dirbrute(url, wordlist):
    """
    Realiza uma busca por diretórios em uma URL usando uma lista de palavras-chave.
    
    Args:
        url (str): A URL base para a busca.
        wordlist (list): Uma lista de palavras-chave para a busca.
    """
    for word in wordlist: # Para cada palavra na wordlist
        word = word.strip() # Removendo os espaços
        url_final = f"{url}/{word}" # Pega a URL passada como argumento e acrescenta uma palavra da wordlist
        response = requests.get(url_final, timeout=5) # Resposta da requisição
        response = response.status_code # Status code da requisição
        try:
            requests.get(url_final, timeout=5) # Faz a requisição com a palavra chave da wordlist
            if response != 404: # Caso o status code seja diferente de 404
                print(url_final, response) # Exibe a URL encontrada e o código da requisição
        except RequestException as error:
            print(error)
        except KeyboardInterrupt:
            print("\n\n\n Tchau :)")
            sys.exit(0)