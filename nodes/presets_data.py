# presets_data.py

import json
import os

with open(os.path.join(os.path.dirname(__file__), "presets.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

def select_brief_by_name(name):
    for preset in data.get("presets", []):
        if preset["name"] == name:
            return preset["brief"]
    return None