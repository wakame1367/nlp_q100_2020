"""
https://nlp100.github.io/ja/ch03.html#21-%E3%82%AB%E3%83%86%E3%82%B4%E3%83%AA%E5%90%8D%E3%82%92%E5%90%AB%E3%82%80%E8%A1%8C%E3%82%92%E6%8A%BD%E5%87%BA
"""
import re
from util import get_text

if __name__ == '__main__':
    pat = re.compile(r'\[\[Category:.*\]\]')
    text = get_text()
    for match in re.finditer(pat, text):
        print(match.group())
