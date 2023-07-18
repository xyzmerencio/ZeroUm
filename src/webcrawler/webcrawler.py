import sys
import requests
from bs4 import BeautifulSoup

CRAWL = []
CRAWLED = set()


def crawl_links(url):
    """
    Realiza uma varredura em um site para coletar todos os links encontrados.

    Args:
        url (str): O URL do site a ser varrido.
    """
    def request(url):
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
        try:
            response = requests.get(url, headers=header, timeout=10)
            return response.text
        except KeyboardInterrupt:
            sys.exit(0)
        except (AttributeError, TypeError):
            pass

    def pegar_links(html):
        links = []
        try:
            soup = BeautifulSoup(html, "html.parser")
            tags_a = soup.find_all("a", href=True)
            for tag in tags_a:
                link = tag["href"]
                if link.startswith("http"):
                    links.append(link)

            return links
        except (AttributeError, TypeError):
            pass

    def crawl():
        while 1:
            if CRAWL:
                url = CRAWL.pop()

                html = request(url)
                if html:
                    links = pegar_links(html)
                    if links:
                        for link in links:
                            if link not in CRAWLED and link not in CRAWL:
                                CRAWL.append(link)

                    print("Encontrado {}".format(url))

                    CRAWLED.add(url)
                else:
                    CRAWLED.add(url)
            else:
                print("Done")
                break

    CRAWL.append(url)
    crawl()
