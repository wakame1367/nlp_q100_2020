"""
https://nlp100.github.io/ja/ch01.html#00-%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E9%80%86%E9%A0%86
"""
import re
from util import get_text

if __name__ == '__main__':
    pat = re.compile(r'\[\[Category:.*\]\]')
    text = get_text()
    for match in re.finditer(pat, text):
        print(match.group())
