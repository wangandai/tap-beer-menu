import json
import logging

# Paths
key_file = "key.json"
subscribers_data = "data/subscribers.json"
data_directory = "data/"

# Logs
listener_log = "logs/listener.log"
server_log = "logs/server.log"

# Menu config
cutoff_abv = 8.0
good_brands = ["deschutes", "founders", "brewlander", "stone", "cloudwater", "rouge", "heretic", "omnipollo"]


def get_bot_token():
    try:
        bt = json.load(open(key_file))["bot_token"]
    except (IOError, ValueError) as e:
        bt = ""
        logging.critical("Could not get bot token: {}".format(e.message))
    return bt






