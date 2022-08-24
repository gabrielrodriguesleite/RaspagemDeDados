from time import sleep
import requests
from parsel import Selector

from tech_news.database import create_news

HEAD = {"User-agent": "Mozilla", "Accept": "text/html"}
TIMEOUT = 3.0


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""

    sleep(1)
    try:
        response = requests.get(url, headers=HEAD, timeout=TIMEOUT)
    except requests.exceptions.Timeout:
        return None
    return None if response.status_code != 200 else response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""

    return [
        links
        for links in Selector(html_content)
        .css("article div a.cs-overlay-link::attr(href)")
        .getall()
    ]


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    return Selector(html_content).css("a.next.page-numbers::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    s = Selector(html_content)
    return {
        "url": s.css("head link[rel=canonical]::attr(href)").get(),
        "title": s.css("h1.entry-title::text").get().strip(),
        "timestamp": s.css("li.meta-date::text").get(),
        "writer": s.css("span.author ::text").get(),
        "comments_count": len(s.css("li.comment").getall()),
        "summary": "".join(
            Selector(s.css("div.entry-content p").get())
            .css("* ::text")
            .getall()
        ).strip(),
        "tags": [tags for tags in s.css("section.post-tags a::text").getall()],
        "category": s.css("div.meta-category span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    URL = "https://blog.betrybe.com/"
    res = []
    while amount > len(res):
        for n in scrape_novidades(fetch(URL)):
            res.append(scrape_noticia(fetch(n)))

        URL = scrape_next_page_link(fetch(URL))

    create_news(res[:amount])
    return res[:amount]
