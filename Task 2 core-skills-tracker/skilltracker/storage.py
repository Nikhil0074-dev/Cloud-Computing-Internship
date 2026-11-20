"""Save and load progress in a simple JSON file."""
import json
import os

EMPTY = {"concepts": [], "practice": [], "projects": [], "feedback": []}


def load(path):
    """Return saved data. If the file does not exist, return empty data."""
    if not os.path.exists(path):
        return {key: [] for key in EMPTY}
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for key in EMPTY:  # make sure every section exists
        data.setdefault(key, [])
    return data


def save(path, data):
    """Write data to the file."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
