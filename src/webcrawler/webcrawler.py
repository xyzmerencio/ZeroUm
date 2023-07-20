import sys
import requests
from bs4 import BeautifulSoup

CRAWL = []  # Lista que armazenará os links a serem varridos.
CRAWLED = set()  # Conjunto que armazenará os links já varridos.

def crawl_links(url):
    """
    Realiza uma varredura em um site para coletar todos os links encontrados.

    Args:
        url (str): O URL do site a ser varrido.
    """
    def request(url):
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}
        try:
            response = requests.get(url, headers=header, timeout=10)  # Realiza uma solicitação HTTP para obter o conteúdo da página.
            return response.text  # Retorna o conteúdo da página.
        except KeyboardInterrupt:  # Trata a interrupção da execução por meio do teclado.
            sys.exit(0)  # Finaliza o programa.
        except (AttributeError, TypeError):  # Trata erros relacionados a atributos e tipos de dados.
            pass

    def pegar_links(html):
        links = []
        try:
            soup = BeautifulSoup(html, "html.parser")  # Cria um objeto BeautifulSoup para analisar o HTML.
            tags_a = soup.find_all("a", href=True)  # Localiza todas as tags <a> que possuem o atributo href.
            for tag in tags_a:
                link = tag["href"]  # Obtém o valor do atributo href, que é o link.
                if link.startswith("http"):  # Verifica se o link começa com "http" para garantir que seja um link absoluto.
                    links.append(link)  # Adiciona o link à lista de links.

            return links  # Retorna a lista de links encontrados na página.
        except (AttributeError, TypeError):  # Trata erros relacionados a atributos e tipos de dados.
            pass

    def crawl():
        while 1:  # Loop infinito para continuar a varredura até que todos os links sejam analisados.
            if CRAWL:  # Verifica se ainda há links a serem varridos.
                url = CRAWL.pop()  # Remove o último link da lista para ser varrido.

                html = request(url)  # Faz uma solicitação HTTP para obter o conteúdo da página.
                if html:  # Verifica se o conteúdo da página foi obtido com sucesso.
                    links = pegar_links(html)  # Extrai todos os links encontrados no conteúdo da página.
                    if links:  # Verifica se há links na página.
                        for link in links:  # Percorre os links encontrados na página.
                            if link not in CRAWLED and link not in CRAWL:  # Verifica se o link não foi varrido anteriormente.
                                CRAWL.append(link)  # Adiciona o link à lista de links a serem varridos.

                    print("Encontrado {}".format(url))  # Exibe uma mensagem informando que o link foi encontrado.

                    CRAWLED.add(url)  # Adiciona o link ao conjunto de links já varridos.
                else:
                    CRAWLED.add(url)  # Adiciona o link ao conjunto de links já varridos caso não haja conteúdo.
            else:
                print("Done")  # Exibe uma mensagem informando que a varredura foi concluída.
                break  # Sai do loop infinito, finalizando a função de varredura.

    CRAWL.append(url)  # Adiciona o link inicial à lista de links a serem varridos.
    crawl()  # Inicia a varredura do site.
