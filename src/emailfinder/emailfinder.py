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
    to_crawl = []
    crawled = set()
    EMAILS = []

    def request(url):
        user_agent = UserAgent().random
        header = {"User-Agent": user_agent}
        try:
            response = requests.get(url, headers=header, timeout=10)
            return response.text
        except KeyboardInterrupt:
            sys.exit(0)
        except requests.RequestException:
            pass

    def get_links(html):
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

    def get_emails(html):
        emails = re.findall(r"\w[\w\.]+\w@\w[\w\.]+\w", html)
        return emails

    def format_email(email):
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+\.*\w*$', email):
            return email.lower()
        else:
            return email

    to_crawl.append(url)
    while to_crawl:
        url = to_crawl.pop()

        html = request(url)
        if html:
            links = get_links(html)
            if links:
                for link in links:
                    if link not in crawled and link not in to_crawl:
                        to_crawl.append(link)

            emails = get_emails(html)
            for email in emails:
                formatted_email = format_email(email)
                if formatted_email not in EMAILS:
                    print(formatted_email)
                    EMAILS.append(formatted_email)

            crawled.add(url)
        else:
            crawled.add(url)

    print("Pronto")

