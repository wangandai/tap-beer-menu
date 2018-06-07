import logging
import config.config as cfg
import json
import sys
from models.menu_section import MenuSection
from models.util import are_lists_equal
from datetime import datetime


class Menu:
    bar = ""
    sections = None
    # notified = False

    def __init__(self, bar="", sections=None):
        self.bar = bar
        self.sections = sections
        if self.sections is None:
            self.sections = []
        # self.notified = False

    def find_good_beers(self):
        sections = [MenuSection(s.section_id, s.title, s.good_beers()) for s in self.sections if len(s.good_beers()) > 0]
        if len(sections) > 0:
            return Menu(self.bar, sections)

    # def notify_good_beers(self):
    #     if self.notified is False:
    #         return self.find_good_beers()
    #     return None

    def data_file(self):
        return cfg.open_data_file(str.lower(self.bar).replace(" ", "") + "_menu.json")

    def load_beers_from_file(self):
        try:
            with open(self.data_file()) as f:
                m = json.load(f)
            self.from_dict(m)
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
        }

    def from_dict(self, d):
        self.bar = d["bar"]
        self.sections = [MenuSection().from_dict(s) for s in d["sections"]]
        return self
