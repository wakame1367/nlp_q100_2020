"""
https://nlp100.github.io/ja/ch01.html#05-n-gram
"""
from typing import Union


def n_gram(_words: Union[str, list], n_split: int):
    for i in range(len(_words) - n_split + 1):
        yield _words[i:i + n_split]


if __name__ == '__main__':
    q = "I am an NLPer"
    # gram
    print(list(n_gram(q, 1)))
    print(list(n_gram(q, 2)))
    print(list(n_gram(q, 3)))
    # word gram
    words = q.split()
    print(list(n_gram(words, 1)))
    print(list(n_gram(words, 2)))
    print(list(n_gram(words, 3)))
