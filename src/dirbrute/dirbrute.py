import requests
import sys


def dirbrute(url, wordlist):
    for word in wordlist:
        word = word.strip()
        url_final = f"{url}/{word}"
        response = requests.get(url_final)
        response = response.status_code
        try:
            requests.get(url_final)
            if response != 404:
                print(url_final, response)
        except Exception as error:
            print(error)
        except KeyboardInterrupt:
            print("\n\n\n Tchau :)")
            sys.exit(0)

