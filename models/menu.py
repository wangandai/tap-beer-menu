import logging
import config.config as cfg
import json
import sys
from models.menu_section import MenuSection
from models.util import are_lists_equal


class Menu:
    bar = ""
    sections = None
    __time_updated = None

    def __init__(self, bar="", sections=None):
        self.bar = bar
        self.sections = sections
        if self.sections is None:
            self.sections = []

    def get_time_updated(self):
        return self.__time_updated

    def find_good_beers(self):
        return [{
            "section": s.title,
            "good_beers": s.good_beers()
        } for s in self.sections if len(s.good_beers()) > 0]

    def is_worth_going(self):
        return len(self.find_good_beers()) > 0

    def data_file(self):
        return cfg.open_data_file(str.lower(self.bar).replace(" ", "") + "_menu.json")

    def load_beers_from_file(self):
        try:
            with open(self.data_file()) as f:
                m = json.load(f)
            self.from_dict(m)
            self.__time_updated = m["__time_updated"]
            logging.info("Menu({}) successfully loaded from file.".format(self.bar))
        except IOError as e:
            logging.info("Data file for {} menu not found: {}".format(self.bar, e))
        except ValueError as e:
            logging.error("Error reading data file for {} menu: {}".format(self.bar, e))

    def save_beers_to_file(self):
        save_data = self.to_dict()
        logging.debug(save_data)
        try:
            with open(self.data_file(), "w+") as f:
                json.dump(save_data, f, indent=4)
            logging.info("Menu({}) successfully saved to file.".format(self.bar))
        except (IOError, ValueError):
            logging.error(save_data)
            logging.error("Error saving data file for {} menu: {}".format(self.bar, sys.exc_info()[0]))

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.bar == other.bar and self.__section_list_eq__(other.sections)
        return False

    def __ne__(self, other):
        """Override the default Unequal behavior"""
        return self.bar != other.bar or not self.__section_list_eq__(other.sections)

    def __section_list_eq__(self, other_sections):
        return are_lists_equal(self.sections, other_sections)

    def to_dict(self):
        return {
            "bar": self.bar,
            "sections": [s.to_dict() for s in self.sections],
            "__time_updated": self.__time_updated,
        }

    def from_dict(self, d):
        self.bar = d["bar"]
        self.sections = [MenuSection().from_dict(s) for s in d["sections"]]
        self.__time_updated = d["__time_updated"]
        return self
