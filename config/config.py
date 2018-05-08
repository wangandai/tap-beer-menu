import json
import logging
import os

# Paths
key_file = "key.json"
subscribers_data = "data/subscribers.json"
data_directory = "data"

# Logs
listener_log = "logs/listener.log"
server_log = "logs/server.log"

# Menu config
cutoff_abv = 7.0
good_brands = ["deschutes", "founders", "brewlander", "stone", "cloudwater", "rouge", "heretic", "omnipollo"]


def get_bot_token():
    try:
        print(os.getcwd())
        bt = json.load(open(os.path.abspath(key_file)))["bot_token"]
    except (IOError, ValueError) as e:
        bt = ""
        logging.critical("Could not get bot token: {}".format(e.message))
    return bt


def open_data_file(filename):
    return os.path.join(data_directory, filename)



