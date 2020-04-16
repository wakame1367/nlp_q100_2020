"""
https://nlp100.github.io/ja/ch03.html#27-%E5%86%85%E9%83%A8%E3%83%AA%E3%83%B3%E3%82%AF%E3%81%AE%E9%99%A4%E5%8E%BB
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
    file_markup = 'ファイル:'
    result = {}
    markup_pat = re.compile(r'\'{2,5}')
    inline_link_pat = re.compile(r'\[\[(?!ファイル:)(.*?)\]\]')
    for t in match_text.split('\n'):
        if sep in t:
            split_text = t.split(' = ')
            key = split_text[0].lstrip('|')
            value = split_text[1]
            remove_text = markup_pat.sub('', value)
            remove_text = inline_link_pat.sub(r'\1', remove_text)
            result[key] = remove_text
    pprint(result)

