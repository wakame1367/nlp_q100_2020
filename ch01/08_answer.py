"""
https://nlp100.github.io/ja/ch01.html#08-%E6%9A%97%E5%8F%B7%E6%96%87
"""
import re


def cipher(word):
    pat = re.compile("[a-z]")
    result = ""
    for w in word:
        match = pat.search(w)
        if match:
            result += chr(219 - ord(w))
        else:
            result += w
    return result


if __name__ == '__main__':
    q = "I am an NLPer"
    print(cipher(q))
