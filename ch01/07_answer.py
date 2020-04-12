"""
https://nlp100.github.io/ja/ch01.html#07-%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%AB%E3%82%88%E3%82%8B%E6%96%87%E7%94%9F%E6%88%90
"""


def template(x, y, z):
    return "{}時の{}は{}".format(x, y, z)


if __name__ == '__main__':
    print(template(x=12, y="気温", z=22.4))
