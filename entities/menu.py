import logging
import config.config as cfg
import json
import sys
from entities.beer import Beer


class Menu:
    name = ""
    beers = []
    good_beers = []
    was_updated = True

    def __init__(self, name):
        self.name = name
        self.load_beers_from_file()
        self.find_good_beers()

    def update_beers(self, beers):
        if not self._beer_lists_are_equal(self.beers, beers):
            self.beers = beers
            self.find_good_beers()
            self.was_updated = True
        else:
            self.was_updated = False

    @staticmethod
    def _beer_lists_are_equal(list1, list2):
        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            if list1[i] != list2[i]:
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