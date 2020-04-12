"""
https://nlp100.github.io/ja/ch01.html#06-%E9%9B%86%E5%90%88
"""
from typing import Union


def n_gram(_words: Union[str, list], n_split: int):
    for i in range(len(_words) - n_split + 1):
        yield _words[i:i + n_split]


if __name__ == '__main__':
    q1 = "paraparaparadise"
    q2 = "paragraph"

    w1 = set(list(n_gram(q1, 2)))
    w2 = set(list(n_gram(q2, 2)))

    print(w1.union(w2))
    print(w1.intersection(w2))
    print(w1.difference(w2))

    q = "se"

    print(q in w1)
    print(q in w2)
