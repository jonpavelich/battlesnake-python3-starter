import json

def get_config():
    with open('src/config.json', 'r') as f:
        config = json.load(f)

    return config