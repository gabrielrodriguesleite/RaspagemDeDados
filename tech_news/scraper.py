from time import sleep
import requests

HEAD = {"User-agent": "Mozilla", "Accept": "text/html"}
TIMEOUT = 3.0


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""

    sleep(1)
    try:
        response = requests.get(url, HEAD, TIMEOUT)
    except requests.exceptions.Timeout:
        return None
    return None if response.status_code != 200 else response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
