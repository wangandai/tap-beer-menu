import logging
import config.config as cfg
import json
import sys
from entities.beer import Beer


class Menu:
    name = ""
    beers = []
    good_beers = []
    was_updated = False

    def __init__(self, name):
        self.name = name

    def update_beers(self, beers):
        if self._beers_have_changed(beers):
            self.beers = beers
            self.find_good_beers()
            self.was_updated = True
            logging.info("Menu({}) was updated.".format(self.name))
        else:
            self.was_updated = False
            logging.info("Menu({}) was not updated.".format(self.name))

    def _beers_have_changed(self, new_beers):
        if len(self.beers) != len(new_beers):
            return False
        for i in range(len(self.beers)):
            if self.beers[i] != new_beers[i]:
                return False
        return True

    def find_good_beers(self):
        good_beers = []
        for beer in self.beers:
            if beer.is_worth_it():
                good_beers.append(beer)
        self.good_beers = good_beers
        return good_beers

    def is_worth_going(self):
        return len(self.good_beers) > 0

    def _data_file(self):
        return cfg.data_directory + self.name + "_menu.json"

    def load_beers_from_file(self):
        try:
            m = json.load(open(self._data_file()))
            self.beers = [Beer(b["name"], b["type"], b["abv"]) for b in m["beers"]]
            logging.info("Menu({}) successfully loaded from file.".format(self.name))
        except IOError as e:
            logging.info("Data file for {} menu not found: {}".format(self.name, e))
        except ValueError as e:
            logging.error("Error reading data file for {} menu: {}".format(self.name, e))

    def save_beers_to_file(self):
        save_data = {"beers": [beer.__dict__ for beer in self.beers]}
        try:
            with open(self._data_file(), "w+") as f:
                json.dump(save_data, f)
            logging.info("Menu({}) successfully saved to file.".format(self.name))
        except:
            print(save_data)
            logging.error("Error saving data file for {} menu: {}".format(self.name, sys.exc_info()[0]))