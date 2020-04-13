"""
https://nlp100.github.io/ja/ch03.html#23-%E3%82%BB%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E6%A7%8B%E9%80%A0
"""
import re

from util import get_text

if __name__ == '__main__':
    sep = "="
    pat = re.compile(r'(==+)(.*)==+')
    text = get_text()
    for match in re.finditer(pat, text):
        print(match.group(0))
        section_sep = match.group(1)
        print(len(section_sep))
