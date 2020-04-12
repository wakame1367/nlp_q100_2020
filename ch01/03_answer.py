"""
https://nlp100.github.io/ja/ch01.html#03-%E5%86%86%E5%91%A8%E7%8E%87
"""
import re

if __name__ == '__main__':
    q = "Now I need a drink, alcoholic of course, after the heavy lectures" \
        " involving quantum mechanics."
    # skip [.,]
    pat = re.compile("[^a-zA-Z]")
    print([len(pat.sub("", word)) for word in q.split()])
