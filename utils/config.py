import os;
import json;

CONFIG_PATH = os.path.expanduser("~/.config/404cli/config.json");

API_BASE="https://api.404nation.com/api/v1"

def save_token(token):
    os.makedirs(os.path.dirname(CONFIG_PATH),exist_ok=True);
    with open(CONFIG_PATH,"w") as f:
        json.dump({"token":token},f)

def load_token():
    try:
        with open(CONFIG_PATH) as f:
            return json.load(f).get("token");
    except:
        return None;