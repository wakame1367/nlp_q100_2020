"""
https://nlp100.github.io/ja/ch01.html#02-%E3%83%91%E3%83%88%E3%82%AB%E3%83%BC%E3%82%BF%E3%82%AF%E3%82%B7%E3%83%BC%E3%83%91%E3%82%BF%E3%83%88%E3%82%AF%E3%82%AB%E3%82%B7%E3%83%BC%E3%83%BC
"""

if __name__ == '__main__':
    q1 = "パトカー"
    q2 = "タクシー"
    q = ""
    for a, b in zip(q1, q2):
        q += a + b
    print(q)
