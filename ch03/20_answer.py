"""
https://nlp100.github.io/ja/ch01.html#00-%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E9%80%86%E9%A0%86
"""
from util import load_json

if __name__ == '__main__':
    wiki_json = load_json()
    query = "イギリス"
    print(wiki_json[wiki_json["title"] == query]["text"].values[0])
