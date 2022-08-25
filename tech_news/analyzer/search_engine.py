from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362
    lis = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(i["title"], i["url"]) for i in lis]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")

    lis = search_news({"timestamp": "/".join(date.split("-")[::-1])})
    return [(i["title"], i["url"]) for i in lis]


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    lis = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [(i["title"], i["url"]) for i in lis]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
