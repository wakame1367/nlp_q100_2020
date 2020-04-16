"""
https://nlp100.github.io/ja/ch03.html#25-%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%AE%E6%8A%BD%E5%87%BA
"""
import re
from util import get_text
from pprint import pprint

if __name__ == '__main__':
    pat = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}',
                     re.MULTILINE + re.DOTALL)
    text = get_text()
    match = pat.findall(text)
    match_text = match[0]
    sep = ' = '
    result = {}
    for t in match_text.split('\n'):
        if sep in t:
            split_text = t.split(' = ')
            key = split_text[0].lstrip('|')
            value = split_text[1]
            result[key] = value
    pprint(result)
    # pat = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?: (?=\n\|) | (?=\n$))',
    #                  re.MULTILINE + re.DOTALL)
    #
    # match = pat.findall(match_text)
    # print(match)
