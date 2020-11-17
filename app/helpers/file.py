import json

# carrega o arquivo de configurações
def load_config():
    with open("app/config.json", "r", encoding="utf8") as f:
        return json.load(f)

