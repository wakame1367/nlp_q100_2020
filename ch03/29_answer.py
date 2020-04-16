"""
https://nlp100.github.io/ja/ch03.html#29-%E5%9B%BD%E6%97%97%E7%94%BB%E5%83%8F%E3%81%AEurl%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B
"""
import re
from pprint import pprint

import requests
from util import get_text

if __name__ == '__main__':
    pat = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}',
                     re.MULTILINE + re.DOTALL)
    text = get_text()
    match = pat.findall(text)
    match_text = match[0]
    sep = ' = '
    result = {}
    markup_pat = re.compile(r'\'{2,5}')
    query = '国旗画像'

    for t in match_text.split('\n'):
        if sep in t:
            split_text = t.split(' = ')
            key = split_text[0].lstrip('|')
            value = split_text[1]
            result[key] = markup_pat.sub('', value)

    file_name = result[query]
    file_name = file_name.replace(" ", "_")

    # https://www.mediawiki.org/wiki/API:Main_page/ja
    media_wiki_endpoint = 'https://www.mediawiki.org/w/api.php'
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": "File:{}".format(file_name),
        "iiprop": "url"
    }
    session = requests.Session()

    response = session.get(media_wiki_endpoint, params=params)
    pprint(response.json())
