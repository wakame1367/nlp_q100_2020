"""
https://nlp100.github.io/ja/ch03.html#24-%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%8F%82%E7%85%A7%E3%81%AE%E6%8A%BD%E5%87%BA
"""
import re
from util import get_text

if __name__ == '__main__':
    pat = re.compile(r'\[\[ファイル:(.*?)(?:\|.*)?\]\]')
    text = get_text()
    for match in re.finditer(pat, text):
        print(match.group(1))
