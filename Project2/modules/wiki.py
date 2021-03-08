import wikipedia as wiki

def search_article(request, lang='en'):
    try:
        wiki.set_lang(lang)
        return wiki.page(wiki.search(request)[0])
    except:
        return None
