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
    for word in wordlist:
        word = word.strip()
        url_final = f"{url}/{word}"
        response = requests.get(url_final, timeout=5)
        response = response.status_code
        try:
            requests.get(url_final, timeout=5)
            if response != 404:
                print(url_final, response)
        except RequestException as error:
            print(error)
        except KeyboardInterrupt:
            print("\n\n\n Tchau :)")
            sys.exit(0)