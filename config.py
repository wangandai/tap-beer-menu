import json

class Config:
    bot_token = ""

    def __init__(self):
        config_data = json.load(open("config.json"))
        self.bot_token = config_data["bot_token"]
        print("Configuration loaded")