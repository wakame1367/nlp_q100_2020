"""
https://nlp100.github.io/ja/ch03.html
"""
import pandas as pd
from pathlib import Path

INPUT_PATH = Path("../resources")
JSON_PATH = INPUT_PATH / "jawiki-country.json.gz"


def load_json():
    return pd.read_json(JSON_PATH, lines=True, compression='infer')
