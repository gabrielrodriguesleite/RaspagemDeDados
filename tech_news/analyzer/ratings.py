from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    ord_alp = sorted(find_news(), key=lambda x: x["title"])
    ord_pop = sorted(ord_alp, key=lambda x: -x["comments_count"])
    return [(i["title"], i["url"]) for i in ord_pop][:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
