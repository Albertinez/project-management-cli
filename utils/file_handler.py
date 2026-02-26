import json
import os

DATA_FILE = "data/storage.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": []}

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {"users": []}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)