import sys
import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def crawl(url):
    """
    Faz uma varredura no site especificado e coleta endereços de e-mail únicos encontrados.

    Args:
        url (str): O URL do site a ser varrido.
    """
    to_crawl = []  # Lista para armazenar os URLs a serem rastreados
    crawled = set()  # Conjunto para armazenar os URLs já rastreados
    EMAILS = []  # Lista para armazenar os endereços de e-mail únicos encontrados

    def request(url):
        """
        Envia uma solicitação HTTP para o URL especificado com um user-agent aleatório.

        Args:
            url (str): O URL para enviar a solicitação.

        Returns:
            str: O conteúdo HTML da página se a solicitação for bem-sucedida, caso contrário, None.
        """
        user_agent = UserAgent().random  # Gera um user-agent aleatório
        header = {"User-Agent": user_agent}  # Define o header da solicitação
        try:
            response = requests.get(url, headers=header, timeout=10)  # Envia a solicitação HTTP
            return response.text  # Retorna o conteúdo HTML da página
        except KeyboardInterrupt:
            sys.exit(0)  # Encerra a execução se o usuário pressionar Ctrl+C
        except requests.RequestException:
            pass  # Continua para o próximo URL em caso de erro na solicitação

    def get_links(html):
        """
        Extrai os links do conteúdo HTML fornecido.

        Args:
            html (str): O conteúdo HTML da página.

        Returns:
            list: Uma lista contendo os links completos encontrados na página.
        """
        links = []
        try:
            soup = BeautifulSoup(html, "html.parser")  # Cria um objeto BeautifulSoup para analisar o HTML
            tags_a = soup.find_all("a", href=True)  # Encontra todas as tags <a> com o atributo href
            for tag in tags_a:
                link = tag["href"]  # Obtém o valor do atributo href
                if link.startswith("http"):  # Verifica se o link é completo (começa com "http")
                    links.append(link)  # Adiciona o link completo à lista

            return links
        except (AttributeError, TypeError):
            pass  # Continua para o próximo URL em caso de erro na extração de links

    def get_emails(html):
        """
        Extrai os endereços de e-mail do conteúdo HTML fornecido usando uma expressão regular.

        Args:
            html (str): O conteúdo HTML da página.

        Returns:
            list: Uma lista contendo os endereços de e-mail encontrados na página.
        """
        emails = re.findall(r"\w[\w\.]+\w@\w[\w\.]+\w", html)  # Encontra todos os endereços de e-mail usando a regex
        return emails

    def format_email(email):
        """
        Formata um endereço de e-mail para garantir que esteja em letras minúsculas e em um formato válido.

        Args:
            email (str): O endereço de e-mail a ser formatado.

        Returns:
            str: O endereço de e-mail formatado.
        """
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+\.*\w*$', email):  # Verifica se o e-mail está em um formato válido
            return email.lower()  # Converte o e-mail para letras minúsculas
        else:
            return email  # Retorna o e-mail original se não estiver em um formato válido

    to_crawl.append(url)  # Adiciona o URL inicial à lista de URLs a serem rastreados
    while to_crawl:
        url = to_crawl.pop()  # Obtém o próximo URL a ser rastreado da lista

        html = request(url)  # Faz uma solicitação HTTP para o URL
        if html:
            links = get_links(html)  # Obtém os links do conteúdo HTML
            if links:
                for link in links:
                    if link not in crawled and link not in to_crawl:
                        to_crawl.append(link)  # Adiciona novos links encontrados à lista de URLs a serem rastreados

            emails = get_emails(html)  # Obtém os endereços de e-mail do conteúdo HTML
            for email in emails:
                formatted_email = format_email(email)  # Formata o endereço de e-mail
                if formatted_email not in EMAILS:  # Verifica se o e-mail já foi coletado
                    print(formatted_email)  # Exibe o endereço de e-mail coletado
                    EMAILS.append(formatted_email)  # Adiciona o e-mail à lista de e-mails coletados

            crawled.add(url)  # Adiciona o URL atual ao conjunto de URLs rastreados
        else:
            crawled.add(url)  # Adiciona o URL atual ao conjunto de URLs rastreados mesmo se não houver conteúdo HTML

    print("Pronto")  # Exibe uma mensagem de conclusão após a varredura ser concluída
