"""
https://nlp100.github.io/ja/ch03.html
"""
import pandas as pd
from pathlib import Path

INPUT_PATH = Path("../resources")
JSON_PATH = INPUT_PATH / "jawiki-country.json.gz"


def load_json():
    return pd.read_json(JSON_PATH, lines=True, compression='infer')


def get_text():
    wiki_json = load_json()
    query = "イギリス"
    return wiki_json[wiki_json["title"] == query]["text"].values[0]
