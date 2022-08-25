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
    ct = [i["category"] for i in find_news()]
    dc = {}
    for j in ct:
        dc[j] = dc[j] + 1 if j in dc else 1

    sort = sorted([(k, dc[k]) for k in dc], key=lambda x: x[0])
    return [s[0] for s in sorted(sort, key=lambda x: -x[1])][:5]
