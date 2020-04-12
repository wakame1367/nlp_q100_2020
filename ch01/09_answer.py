"""
https://nlp100.github.io/ja/ch01.html#09-typoglycemia
"""
import random


def f(_word):
    if len(_word) > 4:
        rand_seq = _word[1:-1]
        rand_words = "".join(random.sample(rand_seq, len(rand_seq)))
        return _word[0] + rand_words + _word[-1]
    return _word


if __name__ == '__main__':
    q = "I couldn’t believe that I could actually understand what I was" \
        " reading : the phenomenal power of the human mind ."
    print("".join(f(word) for word in q.split()))
