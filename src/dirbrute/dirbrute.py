import requests
import threading
import sys


def dirbrute(url, wordlist):
    session = requests.Session()
    lock = threading.Lock()
    total_requests = 0

    def fazer_request(url):
        try:
            response = session.get(url)
            response_code = response.status_code
            return response_code
        except Exception as error:
            print(error)

    def print_resultado(url):
        nonlocal total_requests
        response_code = fazer_request(url)
        if response_code and response_code != 404:
            with lock:
                print(url, response_code)
            total_requests -= 1

    try:
        for word in wordlist:
            word = word.strip()
            url_final = f"{url}/{word}"
            thread = threading.Thread(target=lambda: print_resultado(url_final))
            thread.start()
            total_requests += 1

            while total_requests >= 3:
                pass

        for thread in threading.enumerate():
            if thread != threading.current_thread():
                thread.join()

    except KeyboardInterrupt:
        print("\n\n\n Tchau :)")
        sys.exit(0)