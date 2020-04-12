"""
https://nlp100.github.io/ja/ch01.html#04-%E5%85%83%E7%B4%A0%E8%A8%98%E5%8F%B7
"""

if __name__ == '__main__':
    q = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations" \
        " Might Also Sign Peace Security Clause. Arthur King Can."
    index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    result = {}
    words = q.split()
    for idx, word in enumerate(words, 1):
        if idx in index:
            result[word[0]] = idx
        else:
            result[word[:2]] = idx
    print(result)
