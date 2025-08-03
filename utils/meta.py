import os
import json

META_PATH = os.path.expanduser("~/.config/404cli/.404meta.json")

def save_last_hack_id(hack_id):
    os.makedirs(os.path.dirname(META_PATH), exist_ok=True)
    with open(META_PATH, "w") as f:
        json.dump({"last_id": hack_id}, f)

def load_last_hack_id():
    try:
        with open(META_PATH) as f:
            return json.load(f).get("last_id")
    except:
        return None
