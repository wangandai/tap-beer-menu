import logging
import config.config as cfg
import json
import sys


class Menu:
    name = ""
    beers = []

    def __init__(self, name):
        self.name = name
        self.load_beers_from_file()

    def update_beers(self, beers):
        self.beers = beers

    def is_worth_going(self):
        good_beers = []
        for beer in self.beers:
            if beer.is_worth_it():
                good_beers.append(beer)
        return len(good_beers) > 0, good_beers

    def _data_file(self):
        return cfg.data_directory + self.name + "_menu.json"

    def load_beers_from_file(self):
        try:
            m = json.load(open(self._data_file()))
            self.beers = m["beers"]
            logging.info("Menu({}) successfully loaded from file.".format(self.name))
        except IOError as e:
            logging.info("Data file for {} menu not found: {}".format(self.name, e))
        except ValueError as e:
            logging.error("Error reading data file for {} menu: {}".format(self.name, e))

    def save_beers_to_file(self):
        save_data = {"beers": self.beers}
        try:
            with open(self._data_file(), "w+") as f:
                f.write(json.dumps(save_data))
            logging.info("Menu({}) successfully saved to file.".format(self.name))
        except:
            logging.error("Error saving data file for {} menu: {}".format(self.name, sys.exc_info()[0]))