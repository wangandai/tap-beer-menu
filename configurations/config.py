import json


class Config:
    # Paths
    key_file = "../key.json"
    subscribers_data = "../data/subscribers.json"
    menu_data = "../data/menu.json"

    # Variables
    bot_token = ""

    def __init__(self):
        try:
            self.bot_token = json.load(open(self.key_file))["bot_token"]
        except (IOError, ValueError):
            print("Could not get bot token.")
